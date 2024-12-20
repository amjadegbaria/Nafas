from utils.constants import answered_questions


def already_answered(user_id, question):
    q_id = question.get_id()
    if answered_questions.get(user_id, None) and answered_questions.get(user_id).get(q_id):
        return True
    if answered_questions.get(user_id, None):
        answered_questions[user_id].update({q_id: q_id})
    else:
        answered_questions.update({user_id: {}})
        answered_questions[user_id].update({q_id: q_id})
    return False


def get_chat_id(update):
    if update.callback_query:
        return update.callback_query.message.chat_id
    return update.message.chat_id