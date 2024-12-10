from telegram import Update
from telegram.ext import CallbackContext
from flows.restart_flow import RESTART_FLOW
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
    active = user_data.get('active_flow', None)
    # check if 15min passed, if true, clear the active flow from the DB and restart
    if remove_expired_active_flow(user_data):
        # clean the user from local active_users map
        active_users_map.pop(user_data["_id"])
        if answered_questions.get(user_data["_id"]):
            answered_questions.pop(user_data["_id"])
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