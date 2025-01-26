from utils.constants import answered_questions
import asyncio
import i18n


translate = i18n.Translator('data').translate

def already_answered(user_id, question):
    q_id = ""
    if question:
        q_id = question.get_id()
    if answered_questions.get(user_id, None) and answered_questions.get(user_id).get(q_id):
        return True
    return False


def update_already_answered(user_id, question, answer):
    q_id = question.get_id()
    if answered_questions.get(user_id, None):
        answered_questions[user_id].update({q_id: answer})
    else:
        answered_questions.update({user_id: {}})
        answered_questions[user_id].update({q_id: answer})


def get_chat_id(update):
    if update.callback_query:
        return update.callback_query.message.chat_id
    return update.message.chat_id


async def timer(update, seconds):

    message = update.callback_query.message
    for seconds_left in range(seconds, -1, -1):
        await asyncio.sleep(1)
        await message.edit_text(f" {message.text}:{seconds_left}")


async def complete_the_sentence(update, context):
    # Retrieve answers from the answered_questions dictionary
    answers = answered_questions[update.effective_user.id]
    ans1 = answers.get("task6_12")
    ans2 = answers.get("task6_13")
    ans3 = answers.get("task6_14")
    ans4 = update.callback_query.data or answers.get("task6_14")

    # Translate the sentence, and use f-string formatting
    text = translate("task6_23")  # Here you fetch the static translation text
    formatted_text = text.format(ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4)  # Format the string dynamically

    # Send the formatted text to the chat
    await context.bot.send_message(get_chat_id(update), text=formatted_text)
    return True
