from classes.Flow import Flow
from flows.index import questions_map, flows_map
from database.queries import get_user_progress, save_user_progress, reset_user_progress, save_user_completed_flow, get_user_data

active_users_map = {}

# Start a flow (or restart)
def start_flow(user_id, flow_id, first_question_id):
    active_flow = {
        "flow_id": flow_id,
        "current_question_id": first_question_id,
        "answers": []
    }
    save_user_progress(user_id, active_flow)
    return 0  # Return the index of the first question


# Save the user's answer and move to the next question
def save_answer(user_id, answer, question_id):
    user_progress = get_user_progress(user_id)
    if user_progress:
        user_progress['answers'].append({"question_id": question_id, "answer": answer})
        user_progress['current_question_id'] = question_id
        save_user_progress(user_id, user_progress)
        return user_progress['current_question_id']
    return None


# Resume the flow from where the user left off
def resume_flow(user_id):
    user_progress = get_user_progress(user_id)
    if user_progress:
        return user_progress['current_question_id']
    return None


# Restart the flow
def restart_flow(user_id, flow_id, first_question_id):
    return start_flow(user_id, flow_id, first_question_id)


def complete_flow(user_id):
    user_progress = get_user_progress(user_id)
    save_user_completed_flow(user_id, user_progress)


def get_next_from_answer(update, question):
    if len(question.get_options()) == 0:  # if no buttons, get the next question from next_question_id
        return question.next_question_id
    query = update.callback_query
    if query:  # if user clicks a button, direct to the next question according to the user choice
        return question.get_next_question(query.data)
    text = update.message.text
    return question.get_next_question(text)


def get_user_flow(user_id):
    if active_users_map.get(user_id, None):
        return active_users_map[user_id]

    user_data = get_user_data(user_id)
    if user_data:
        active = user_data.get('active_flow', None)
        completed = user_data.get('completed_flows', None)
        if active:
            flow_id = active.get('flow_id')
            current_question_id = active.get('current_question_id')
            active_users_map[user_id] = Flow(flow_id, questions_map[flow_id], current_question_id)
            return active_users_map[user_id]
        elif completed:
            last_completed_id = completed[len(completed) - 1].get('flow_id')
            flow_id = flows_map[last_completed_id]
            questions = questions_map[flow_id]
            active_users_map[user_id] = Flow(flow_id, questions)
            return active_users_map[user_id]
