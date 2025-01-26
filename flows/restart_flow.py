import i18n
from classes.Question import Question
from classes.Flow import Flow
from database.queries import reset_user_progress
from utils.constants import active_users_map, answered_questions
from handlers.utils import process_question, get_user_flow, start_flow


async def restart_flow(update, context):
    user_id = update.effective_user.id
    reset_user_progress(user_id)  # clean the restart flow from the DB
    if active_users_map.get(user_id):
        active_users_map.pop(user_id)
    if answered_questions.get(user_id):
        answered_questions.pop(user_id)

    flow = get_user_flow(user_id)
    flow.start_flow(flow.get_first_question_id())
    start_flow(user_id, flow.get_id(), flow.get_first_question_id())

    RESTART_FLOW.start_flow(RESTART_FLOW.get_first_question_id())
    # Process the first question in the flow
    await process_question(update, context, flow)

translate = i18n.Translator('data').translate

questions = {
    "restart": Question(
        id="restart",
        text=translate("restart_message"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="restart2"
    ),
    "restart2": Question(
        id="restart2",
        text=translate("restart_message2"),
        media="",
        media_type="",
        options={translate("restart_button"): restart_flow},
        keyboard_type="inline",
        next_question_id=""
    )
}

RESTART_FLOW = Flow('restart_flow', questions, "restart")
