from telegram import Update
from telegram.ext import  CallbackContext, ContextTypes
from flows.Flow3 import flow
from handlers.message_handler import handle_media, handle_message, answered_questions

async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    flow.start_flow("intro1")  # Start with the first question
    question = flow.get_current_question()
    await handle_media(question, update, context)

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