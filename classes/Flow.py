class Flow:
    def __init__(self, questions: dict):
        """
        Initializes the flow with a dictionary of questions.
        The dictionary keys are question IDs and values are Question objects.
        """
        self.questions = questions
        self.current_index = -1
        self.history = []

    def get_current_question(self):
        if self.current_index >= 0:
            current_id = self.history[self.current_index]
            return self.questions.get(current_id)
        return None

    def move_to_next_question(self, next_question_id: str):
        self.current_index += 1
        if next_question_id:
            self.history.append(next_question_id)
            return self.questions.get(next_question_id)
        else:
            self.history.append(self.questions[self.current_index])
            return self.questions[self.current_index]


    def start_flow(self, start_question_id: str):
        """
        Starts the flow from a specific question.
        """
        self.history = [start_question_id]
        self.current_index = 0