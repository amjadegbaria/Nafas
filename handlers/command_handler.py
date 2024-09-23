from telegram import Update
from telegram.ext import  CallbackContext
from flows.Flow3 import flow
from handlers.message_handler import handle_media
async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    flow.start_flow("intro1")  # Start with the first question
    question = flow.get_current_question()
    await handle_media(question, update, context)
