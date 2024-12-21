from telegram import Update
from telegram.ext import CallbackContext
from _datetime import datetime
from flows.restart_flow import RESTART_FLOW
from flows.menu_flow import menu_flow
from database.queries import get_user_progress, remove_expired_active_flow
from utils.constants import active_users_map, answered_questions
from handlers.utils import process_question, start_flow


# Resume the flow from where the user left off
def resume_flow(user_id):
    user_progress = get_user_progress(user_id)
    if user_progress:
        return user_progress['current_question_id']
    return None


def check_user_last_interaction(user_data):
    # check if 15min passed, if true, clear the active flow from the DB and restart
    if remove_expired_active_flow(user_data):
        # clean the user from local active_users map
        active_users_map.pop(user_data["_id"])
        if answered_questions.get(user_data["_id"]):
            answered_questions.pop(user_data["_id"])
        return True


# if the user completed the flow for today, return true
def is_flow_done_today(user_data):
    completed_flows = user_data.get('completed_flows')
    active_flow = user_data.get('active_flow')
    if not active_flow and completed_flows and completed_flows[-1]:
        last_flow = completed_flows[-1]
        last_interaction = last_flow['last_interaction'].strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        date = datetime.fromisoformat(last_interaction)
        if date.date() == date.utcnow().date():
            return True


async def trigger_restart_flow(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    # Start the restart flow
    question = RESTART_FLOW.get_current_question()
    RESTART_FLOW.start_flow(question.get_id())
    start_flow(user_id, RESTART_FLOW.get_id(), question.get_id())
    active_users_map[user_id] = RESTART_FLOW

    # Process the first question in the restart flow
    await process_question(update, context, RESTART_FLOW)


async def trigger_menu_flow(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    flow = menu_flow.duplicate_flow()
    # Start the restart flow
    question = menu_flow.get_current_question()
    flow.start_flow(question.get_id())
    start_flow(user_id, flow.get_id(), question.get_id())
    active_users_map[user_id] = flow

    # Process the first question in the restart flow
    await process_question(update, context, flow)
