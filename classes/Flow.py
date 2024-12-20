class Flow:
    def __init__(self, flow_id: str, questions: dict, current_question_id="", first_question_id=None):
        """
        Initializes the flow with a dictionary of questions.
        The dictionary keys are question IDs and values are Question objects.
        """
        self.id = flow_id
        self.questions = questions
        self.current_question_id = current_question_id
        self.first_question_id = first_question_id or current_question_id

    def get_current_question(self):
        return self.questions.get(self.current_question_id)

    def get_id(self):
        return self.id

    def move_to_next_question(self, next_question_id: str):
        if next_question_id:
            self.current_question_id = next_question_id
            return self.questions.get(next_question_id)
        return None

    def start_flow(self, start_question_id: str):
        """
        Starts the flow from a specific question.
        """
        self.current_question_id = start_question_id

    def is_completed(self):
        if self.get_current_question().is_last():
            return True
        return False

    def get_question_by_id(self, q_id):
        return self.questions.get(q_id)

    def get_first_question_id(self):
        return self.first_question_id

    def duplicate_flow(self):
        return Flow(self.id, self.questions, self.current_question_id, self.first_question_id)