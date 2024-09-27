from time import sleep
from telegram import Update, constants
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext, ContextTypes
import logging
import i18n
from flows.Flow3 import flow
from flows.flow_handler import start_flow, save_answer, complete_flow
from database.__init__ import client

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your bot token
TOKEN = '7304026680:AAHT8Am89N6s-fYE5FYA799VdboO9V29jbk'
application = Application.builder().token(TOKEN).build()

translator = i18n.Translator('data')

answered_questions = {}


def already_answered(question):
    if answered_questions.get(question._id):
        return True
    answered_questions[question._id] = question._id
    return False

# Initialize Flow

def getChatID(update):
    if update.callback_query:
        return update.callback_query.message.chat_id
    return update.message.chat_id

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


async def handle_media(question, update, context) :
    if already_answered(question):
        return

    if question:
        # Prepare the text and markup
        text = question.get_question_text()
        markup = question.get_markup()

        # Prepare media based on media type
        media_path = question._media
        media_type = question.get_media_type()
        chat_id = getChatID(update)

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
        elif media_type == 'youtube':
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"{text}\n{media_path}",
                reply_markup=markup,
            )
        elif media_type== 'game':
            # Handle game integration here
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"{text}\n{media_path}",
                reply_markup=markup,
            )
        elif len(question.get_options()) == 0:
            await context.bot.send_message(chat_id=chat_id, text=text)
            # sleep(2)
        else:
            await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=markup)
        if len(question.get_options()) == 0:
            # sleep(2)
            await handle_message(update, context)

    else:
        await update.message.reply_text("Sorry, I don't understand that answer.")
async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    """Handle the /start command."""
    flow.start_flow("intro1")  # Start with the first question
    start_flow(user_id, flow.get_flow_id(), "intro1")
    # check_mongo_connection()
    question = flow.get_current_question()
    await handle_media(question, update, context)


def get_next_from_answer(update, question):
    if len(question.get_options()) == 0: ## if no buttons, get the next question from next_question_id
        return question.next_question_id
    query = update.callback_query
    if query: ## if user clicks a button, direct to the next question according to the user choice
        return question.get_next_question(query.data)
    text = update.message.text
    next = question.get_next_question(text)
    if next == None:
        complete_flow(update.effective_user.id)
    return next
async def handle_message(update: Update, context: CallbackContext) -> None:
    question = flow.get_current_question()
    if len(question.get_options()) > 0: # if there are options(buttons), save the response in the DB
        update_user_answer(update)
    """Handle replies to reply keyboards."""
    next_question_id = get_next_from_answer(update, flow.get_current_question())
    if flow.is_completed():
        complete_flow(update.effective_user.id)
    next_question = flow.move_to_next_question(next_question_id)
    await handle_media(next_question, update, context)


async def restart(update: Update, context: CallbackContext) -> None:
    flow.start_flow("intro")
    answered_questions.clear()
    await start(update, context)

async def default(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(answered_questions) == 0:
        await start(update, context)
    elif answered_questions.get("end_1"): ## if the user reachs the last question, restart
        await restart(update, context)
    else:
        await handle_message(update, context)




def main() -> None:
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("restart", restart))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, default))
    application.add_handler(CallbackQueryHandler(handle_message))

    # Start the Bot
    application.run_polling()


if __name__ == '__main__':
    import asyncio

    try:
        asyncio.run(main())
    except KeyboardInterrupt:  # Ignore exception when Ctrl-C is pressed
        pass