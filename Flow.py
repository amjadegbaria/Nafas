import Question


class Flow:
    def __init__(self, question=[]):
        self.questions = question
        self.current_index = -1

    def add_question(self, question: Question):
        self.questions.append(question)

    def get_next_question(self):
        self.current_index += 1
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        else:
            return None

    def get_previous_question(self):
        self.current_index -= 1
        if self.current_index >= 0:
            return self.questions[self.current_index]
        else:
            self.current_index = 0
            return None

    def reset(self):
        self.current_index = -1
