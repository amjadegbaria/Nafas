from telegram import Update
from telegram.ext import  CallbackContext, ContextTypes
from flows.Flow3 import flow
from handlers.message_handler import handle_media, handle_message, answered_questions
from flows.flow_handler import start_flow


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    """Handle the /start command."""
    flow.start_flow("intro1")  # Start with the first question
    start_flow(user_id, flow.get_flow_id(), "intro1")
    question = flow.get_current_question()
    await handle_media(question, update, context)


async def restart(update: Update, context: CallbackContext) -> None:
    flow.start_flow("intro")
    answered_questions.clear()
    await start(update, context)


async def default(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(answered_questions) == 0:
        await start(update, context)
    elif flow.get_current_question().is_last():  # if the user reaches the last question, restart
        await restart(update, context)
    else:
        await handle_message(update, context)
