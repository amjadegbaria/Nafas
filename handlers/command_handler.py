from telegram import Update
from telegram.ext import CallbackContext, ContextTypes
from utils.constants import answered_questions
from handlers.flow_handler import start_flow, check_user_last_interaction, process_question, trigger_restart_flow
from handlers.utils import get_user_flow
from database.queries import get_user_data, reset_user_progress


async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    user_id = update.effective_user.id

    # Initialize the user's flow
    flow = get_user_flow(user_id)
    question = flow.get_current_question()
    flow.start_flow(question.get_id())
    start_flow(user_id, flow.get_id(), question.get_id())

    # Process the first question in the flow
    await process_question(update, context, flow)


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
        await process_question(update, context)


async def restart(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    answered_questions.pop(user_id)
    reset_user_progress(user_id)  # clean the restart flow from the DB
    await start(update, context)