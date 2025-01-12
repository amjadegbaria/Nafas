from telegram import Update
from telegram.ext import CallbackContext, ContextTypes
from utils.constants import answered_questions
from handlers.flow_handler import start_flow, check_user_last_interaction, process_question, trigger_restart_flow, is_flow_done_today, trigger_menu_flow
from handlers.utils import get_user_flow
from database.queries import get_user_data, reset_user_progress
from utils.constants import active_users_map
from flows.questions_list import questions_list_flow

async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    user_id = update.effective_user.id
    reset_user_progress(user_id)  # clean the restart flow from the DB
    if active_users_map.get(user_id):
        active_users_map.pop(user_id)
    if answered_questions.get(user_id):
        answered_questions.pop(user_id)

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

    if is_flow_done_today(user_data):
        await trigger_menu_flow(update, context)
    elif check_user_last_interaction(user_data):
        await trigger_restart_flow(update, context)
    elif not answered_questions.get(user_id, None):  # flow did not start yet
        await start(update, context)
    else:
        await process_question(update, context)


async def restart(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    reset_user_progress(user_id)  # clean the restart flow from the DB
    if active_users_map.get(user_id):
        active_users_map.pop(user_id)
    if answered_questions.get(user_id):
        answered_questions.pop(user_id)

    flow = get_user_flow(user_id)
    flow.start_flow(flow.get_first_question_id())
    start_flow(user_id, flow.get_id(), flow.get_first_question_id())

    # Process the first question in the flow
    await process_question(update, context, flow)

async def menu(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    reset_user_progress(user_id)  # clean the restart flow from the DB
    if active_users_map.get(user_id):
        active_users_map.pop(user_id)
    if answered_questions.get(user_id):
        answered_questions.pop(user_id)
    flow = questions_list_flow.duplicate_flow()
    flow.start_flow(flow.get_first_question_id())
    start_flow(user_id, flow.get_id(), flow.get_first_question_id())
    active_users_map[user_id] = flow
    await process_question(update, context, flow)
