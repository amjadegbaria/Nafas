class Flow:
    def __init__(self, flow_id: str, questions: dict):
        """
        Initializes the flow with a dictionary of questions.
        The dictionary keys are question IDs and values are Question objects.
        """
        self.id = flow_id
        self.questions = questions
        self.current_question_id = ""
        self.history = []

    def get_current_question(self):
        return self.questions.get(self.current_question_id)


    def get_flow_id(self):
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
        return self.questions[q_id]
