from utils.constants import answered_questions


def already_answered(user_id, question):
    q_id = question.get_id()
    if answered_questions.get(user_id, None) and answered_questions.get(user_id).get(q_id):
        return True
    return False


def update_already_answered(user_id, question):
    q_id = question.get_id()
    if answered_questions.get(user_id, None):
        answered_questions[user_id].update({q_id: q_id})
    else:
        answered_questions.update({user_id: {}})
        answered_questions[user_id].update({q_id: q_id})


def get_chat_id(update):
    if update.callback_query:
        return update.callback_query.message.chat_id
    return update.message.chat_id
async def timer(update, seconds):
    # from utils.helpers import get_chat_id
    import asyncio
    new_message = update.callback_query.message
    for seconds_left in range(seconds - 1, -1, -1):
        await asyncio.sleep(1)
        await new_message.edit_text(text=f" {new_message.text}:{seconds_left}")
    return

