from _datetime import datetime
from asyncio import sleep
from telegram import Update
from telegram.ext import CallbackContext
from flows.index import flows_map, initial_flow, flows
from database.queries import get_user_progress, save_user_progress,\
    save_user_completed_flow, get_user_data, get_user_answer, reset_user_progress
from handlers.media_handler import handle_media_type
from utils.helpers import already_answered
from utils.constants import active_users_map, answered_questions

async def restart_flow(update, context):
    user_id = update.effective_user.id
    reset_user_progress(user_id)  # clean the restart flow from the DB
    active_users_map.pop(user_id)
    flow = get_user_flow(user_id)
    question = flow.get_current_question()
    flow.start_flow(question.get_id())
    start_flow(user_id, flow.get_id(), question.get_id())

    # Process the first question in the flow
    await process_question(update, context, flow)

def start_flow(user_id, flow_id, first_question_id):
    if flow_id == 'restart_flow':
        return
    active_flow = {
        "flow_id": flow_id,
        "current_question_id": first_question_id,
        "answers": []
    }
    save_user_progress(user_id, active_flow)
    return 0  # Return the index of the first question


def get_next_from_answer(update, question):
    if len(question.get_options()) == 0:  # if no buttons, get the next question from next_question_id
        return question.next_question_id
    query = update.callback_query
    if query:  # if user clicks a button, direct to the next question according to the user choice
        return question.get_next_question(query.data)
    text = update.message.text
    return question.get_next_question(text)


def complete_flow(user_id):
    user_progress = get_user_progress(user_id)
    save_user_completed_flow(user_id, user_progress)
    active_users_map.pop(user_id)


def is_completed(flow, user_id):
    if flow.is_completed():  # if flow completed, save the response and restart the flow
        answered_questions.pop(user_id)
        # if the completed flow is the restart flow, clean the active flow and move to next one
        if flow.get_id() == "restart_flow":
            reset_user_progress(user_id)
        else:
            complete_flow(user_id)


def save_answer(user_id, answer, question_id):
    user_progress = get_user_progress(user_id)
    user_progress['answers'] = user_progress.get('answers', {})
    user_progress['answers'].append({"question_id": question_id, "answer": answer})
    user_progress['current_question_id'] = question_id
    save_user_progress(user_id, user_progress)
    return user_progress['current_question_id']


def update_user_answer(update):
    user_id = update.effective_user.id
    flow = get_user_flow(user_id)
    question = flow.get_current_question()
    current_question_id = question.get_id()
    user_id = get_user_answer(update)["user_id"]
    answer = get_user_answer(update)["answer"]
    save_answer(user_id, answer, f"{current_question_id}")


def get_user_flow(user_id):
    user_data = get_user_data(user_id)
    if active_users_map.get(user_id, None):
        return active_users_map[user_id]

    if user_data:
        active = user_data.get('active_flow', None)
        completed = user_data.get('completed_flows', None)
        if active:
            flow_id = active.get('flow_id')
            current_flow_id = active.get('current_flow_id')
            active_users_map[user_id] = flows.get(flow_id).duplicate_flow(current_flow_id)
            return active_users_map[user_id]
        elif completed:
            last_completed_id = completed[len(completed) - 1].get('flow_id')
            next_flow_id = flows_map[last_completed_id]
            last_flow = completed[-1]
            last_interaction = last_flow['last_interaction'].strftime("%Y-%m-%dT%H:%M:%S.%f%z")
            date = datetime.fromisoformat(last_interaction)
            if date.date() == date.utcnow().date():
                active_users_map[user_id] = flows.get(last_completed_id).duplicate_flow()
            else:
                active_users_map[user_id] = flows.get(next_flow_id).duplicate_flow()
            return active_users_map[user_id]

    active_users_map[user_id] = flows.get(initial_flow).duplicate_flow('intro1')
    return active_users_map[user_id]


async def process_question(update: Update, context: CallbackContext, flow=None) -> None:
    user_id = update.effective_user.id

    # Retrieve or initialize the flow
    if not flow:
        flow = get_user_flow(user_id)

    question = flow.get_current_question()

    # Check if the question has already been answered
    if already_answered(user_id, question):
        return

    # Handle media for the current question
    await handle_media_type(question, update, context)


    # Check if the flow is completed
    if is_completed(flow, user_id):
        return

    # Move to the next question in the flow
    if len(question.get_options()) == 0:
        # Get the next question
        next_question_id = get_next_from_answer(update, question)

        next_question = flow.move_to_next_question(next_question_id)
        if next_question:
            await sleep(2)
            await process_question(update, context, flow)
