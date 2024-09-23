
def getNextFromAnswer(update, question):
    if len(question.get_options()) == 0:
        return question.next_question_id
    query = update.callback_query
    if query:
        return query.data
    text = update.message.text
    return question.get_next_question(text)