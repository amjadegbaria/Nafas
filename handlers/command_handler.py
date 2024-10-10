from telegram import Update
from telegram.ext import  CallbackContext, ContextTypes
# from flows.Flow3 import flow
from handlers.message_handler import handle_media, handle_message, answered_questions
from flows.flow_handler import start_flow, get_user_flow

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    """Handle the /start command."""
    flow = get_user_flow(user_id)
    question = flow.get_current_question()
    flow.start_flow(question.get_id())  # Start with the first question
    start_flow(user_id, flow.get_flow_id(), question.get_id())
    await handle_media(question, update, context)


async def restart(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    flow = get_user_flow(user_id)
    flow.start_flow("intro")
    answered_questions.clear()
    await start(update, context)


async def default(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    flow = get_user_flow(user_id)
    if not answered_questions.get(user_id, None):  # flow did not start yet
        await start(update, context)
    elif flow.is_completed():  # if the user reaches the last question, restart
        await restart(update, context)
    else:
        await handle_message(update, context)
