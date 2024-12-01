from classes.Flow import Flow
from flows.index import questions_map, flows_map, initial_flow
from database.queries import get_user_progress, save_user_progress, remove_expired_active_flow, \
    save_user_completed_flow, get_user_data

active_users_map = {}
answered_questions = {}


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
    user_progress['answers'].append({"question_id": question_id, "answer": answer})
    user_progress['current_question_id'] = question_id
    save_user_progress(user_id, user_progress)
    return user_progress['current_question_id']


# Resume the flow from where the user left off
def resume_flow(user_id):
    user_progress = get_user_progress(user_id)
    if user_progress:
        return user_progress['current_question_id']
    return None


def complete_flow(user_id):
    user_progress = get_user_progress(user_id)
    save_user_completed_flow(user_id, user_progress)
    active_users_map.pop(user_id)


def get_next_from_answer(update, question):
    if len(question.get_options()) == 0:  # if no buttons, get the next question from next_question_id
        return question.next_question_id
    query = update.callback_query
    if query:  # if user clicks a button, direct to the next question according to the user choice
        return question.get_next_question(query.data)
    text = update.message.text
    return question.get_next_question(text)


def check_user_last_interaction(user_data):
    active = user_data.get('active_flow', None)
    # check if 15min passed, if true, clear the active flow from the DB and restart
    if active and remove_expired_active_flow(user_data):
        # clean the user from local active_users map
        active_users_map.pop(user_data["_id"])
        answered_questions.pop(user_data["_id"])
        return True


def get_user_flow(user_id):
    user_data = get_user_data(user_id)
    if active_users_map.get(user_id, None):
        return active_users_map[user_id]

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
            active_users_map[user_id] = Flow(flow_id, questions, list(questions.keys())[0])
            return active_users_map[user_id]
    else:
        questions = questions_map[initial_flow]
        active_users_map[user_id] = Flow(initial_flow, questions, list(questions.keys())[0])
        return active_users_map[user_id]
