import i18n
from classes.Question import Question
from classes.Flow import Flow
from database.queries import reset_user_progress
from utils.constants import active_users_map, answered_questions
from handlers.utils import process_question, start_flow
from flows.questions_list import questions_list_flow


async def menu_flow(update, context):
    flow = questions_list_flow.duplicate_flow('questions_list_intro')
    user_id = update.effective_user.id
    reset_user_progress(user_id)  # clean the menu flow from the DB
    active_users_map.pop(user_id)
    active_users_map[user_id] = flow
    start_flow(user_id, flow.get_id(), flow.get_first_question_id())
    answered_questions.pop(user_id)
    flow.start_flow(flow.get_first_question_id())
    # Process the first question in the flow
    await process_question(update, context, flow)

translate = i18n.Translator('data').translate

questions = {
    "menu_flow_1": Question(
        id="menu_flow_1",
        text=translate("menu_flow_1"),
        media="",
        media_type="",
        options={translate("menu_button"): menu_flow},
        keyboard_type="inline",
        next_question_id=""
    ),
}

menu_flow = Flow('menu_flow', questions, "menu_flow_1")
