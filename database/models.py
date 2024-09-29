class User:
    def __init__(self, user_id, username):
        self._id = user_id
        self.username = username
        self.active_flow = None  # Track ongoing flow
        self.completed_flows = []  # Store completed flows

class Flow:
    def __init__(self, flow_id, flow_name, questions):
        self._id = flow_id
        self.flow_name = flow_name
        self.questions = questions
