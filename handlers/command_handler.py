from telegram import Update
from telegram.ext import CallbackContext, ContextTypes
from handlers.message_handler import handle_media, handle_message, answered_questions, trigger_restart_flow
from flows.flow_handler import start_flow, get_user_flow, check_user_last_interaction
from database.queries import get_user_data, reset_user_progress


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    """Handle the /start command."""
    flow = get_user_flow(user_id)
    question = flow.get_current_question()
    flow.start_flow(question.get_id())  # Start with the first question
    start_flow(user_id, flow.get_id(), question.get_id())
    await handle_media(question, update, context)


async def restart(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    flow = get_user_flow(user_id)
    flow.start_flow("intro")
    answered_questions.clear()
    await start(update, context)


async def default(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    user_data = get_user_data(user_id)
    flow = get_user_flow(user_id)

    if check_user_last_interaction(user_data):
        await trigger_restart_flow(update, context)
    elif not answered_questions.get(user_id, None):  # flow did not start yet
        await start(update, context)
    elif flow.is_completed():  # if the user reaches the last question, restart
        await restart(update, context)
    else:
        await handle_message(update, context)

async def restart_flow(update, context):
    user_id = update.effective_user.id
    reset_user_progress(user_id)  # clean the restart flow from the DB
    await start(update, context)