from time import sleep
from telegram import Update
from telegram.ext import CallbackContext
from flows.Flow3 import flow
from flows.flow_handler import save_answer, complete_flow, get_next_from_answer


answered_questions = {}


def already_answered(question):
    q_id = question.get_id()
    if answered_questions.get(q_id):
        return True
    answered_questions[q_id] = q_id
    return False


def get_user_answer(update):
    if update.callback_query:
        return {"answer": update.callback_query.data, "user_id": update.callback_query.from_user.id}
    return {"answer": update.message.text, "user_id": update.message.from_user.id}


def update_user_answer(update):
    question = flow.get_current_question()
    current_question_id = question.get_id()
    user_id = get_user_answer(update)["user_id"]
    answer = get_user_answer(update)["answer"]
    save_answer(user_id, answer, f"{current_question_id}")


async def handle_message(update: Update, context: CallbackContext) -> None:
    question = flow.get_current_question()
    if len(question.get_options()) > 0:  # if there are options(buttons), save the response in the DB
        update_user_answer(update)

    """Handle replies to reply keyboards."""
    next_question_id = get_next_from_answer(update, question)
    if flow.is_completed():  # if flow completed, save the response and restart the flow
        complete_flow(update.effective_user.id)
        flow.start_flow("intro")
        answered_questions.clear()

    next_question = flow.move_to_next_question(next_question_id)
    await handle_media(next_question, update, context)


async def handle_callback_query(update: Update, context: CallbackContext) -> None:
    """Handle callback queries from inline keyboards."""
    query = update.callback_query
    answer = query.data
    next_question = flow.move_to_next_question(answer)
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
            reply_markup=markup
        )
    else:
        await context.bot.send_message(chat_id=chat_id, text=f"{text}\n{media_path}", reply_markup=markup)


async def handle_media(question, update, context) :
    if already_answered(question):  # question is already answered, ignore any button interaction
        return

    if question:
        await handle_media_type(question, update, context)

        if len(question.get_options()) == 0:  # if no options (buttons) defined, continue to next question
            sleep(2)
            await handle_message(update, context)
