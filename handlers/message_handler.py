from time import sleep
from telegram import Update, constants
from telegram.ext import CallbackContext
from flows.restart_flow import RESTART_FLOW
from flows.flow_handler import save_answer, complete_flow, get_next_from_answer, get_user_flow, answered_questions,\
    check_user_last_interaction, start_flow
from database.queries import get_user_data, reset_user_progress


def is_completed(flow, user_id):
    if flow.is_completed():  # if flow completed, save the response and restart the flow
        answered_questions.pop(user_id)
        # if the completed flow is the restart flow, clean the active flow and move to next one
        if flow.get_id() == "restart_flow":
            reset_user_progress(user_id)
        else:
            complete_flow(user_id)


def already_answered(user_id, question):
    q_id = question.get_id()
    if answered_questions.get('user_id', None) and answered_questions[user_id].get(q_id):
        return True
    if answered_questions.get('user_id', None):
        answered_questions[user_id].update({q_id: q_id})
    else:
        answered_questions.update({user_id: {}})
        answered_questions[user_id].update({q_id: q_id})
    return False


async def trigger_restart_flow(update, context):
    user_id = update.effective_user.id
    question = RESTART_FLOW.get_current_question()
    RESTART_FLOW.start_flow(question.get_id())  # Start with the first question
    start_flow(user_id, RESTART_FLOW.get_id(), question.get_id())
    await handle_media(question, update, context)


def get_user_answer(update):
    if update.callback_query:
        return {"answer": update.callback_query.data, "user_id": update.callback_query.from_user.id}
    return {"answer": update.message.text, "user_id": update.message.from_user.id}


def update_user_answer(update):
    user_id = update.effective_user.id
    flow = get_user_flow(user_id)
    question = flow.get_current_question()
    current_question_id = question.get_id()
    user_id = get_user_answer(update)["user_id"]
    answer = get_user_answer(update)["answer"]
    save_answer(user_id, answer, f"{current_question_id}")


async def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    flow = get_user_flow(user_id)
    question = flow.get_current_question()
    if len(question.get_options()) > 0:  # if there are options(buttons), save the response in the DB
        update_user_answer(update)

    is_completed(flow, user_id)  # if flow completed, save the response and restart the flow
    next_question_id = get_next_from_answer(update, question)
    next_question = flow.move_to_next_question(next_question_id)
    await handle_media(next_question, update, context)


async def handle_callback_query(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_data = get_user_data(user_id)
    if check_user_last_interaction(user_data):
        await trigger_restart_flow(update, context)
        return
    answer = get_user_answer(update)["answer"]
    if callable(answer):  # check if function, if yes run it otherwise continue
        answer(update, context)
        return

    flow = get_user_flow(user_id)

    update_user_answer(update)
    is_completed(flow, user_id) # if flow completed, save the response and restart the flow

    """Handle replies to reply keyboards."""
    question = flow.get_current_question()
    next_question_id = get_next_from_answer(update, question)
    next_question = flow.move_to_next_question(next_question_id)
    await handle_media(next_question, update, context)


def get_chat_id(update):
    if update.callback_query:
        return update.callback_query.message.chat_id
    return update.message.chat_id


async def handle_media_type(question, update, context):
    # Prepare the text and markup
    text = question.get_question_text()
    markup = question.get_markup()

    # Prepare media based on media type
    media_path = question._media
    media_type = question.get_media_type()
    chat_id = get_chat_id(update)

    if media_type == 'image':
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=open(media_path, 'rb'),
            caption=text,
            reply_markup=markup
        )
    elif media_type == 'video':
        await context.bot.send_video(
            chat_id=chat_id,
            video=open(media_path, 'rb'),
            caption=text,
            reply_markup=markup,
            read_timeout=200
        )
    elif media_type == 'html':
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"{text}\n{media_path}",
            reply_markup=markup,
            parse_mode=constants.ParseMode.HTML
        )
    elif media_type == 'youtube':
        if media_path:
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"<a href='{media_path}'> </a>{text}",
                reply_markup=markup,
                parse_mode=constants.ParseMode.HTML
            )
    else:
        await context.bot.send_message(chat_id=chat_id, text=f"{text}\n{media_path}", reply_markup=markup, disable_web_page_preview=True)


async def handle_media(question, update, context) :
    if already_answered(update.effective_user.id, question):  # question is already answered, ignore any button interaction
        return

    if question:
        await handle_media_type(question, update, context)

        if len(question.get_options()) == 0:  # if no options (buttons) defined, continue to next question
            sleep(2)
            await handle_message(update, context)
