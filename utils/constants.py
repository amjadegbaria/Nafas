import asyncio
from collections import defaultdict

# Thread-safe state management
class ThreadSafeState:
    def __init__(self):
        self._lock = asyncio.Lock()
        self._active_users_map = {}
        self._answered_questions = defaultdict(set)
    
    async def get_active_user(self, user_id):
        async with self._lock:
            return self._active_users_map.get(user_id)
    
    async def set_active_user(self, user_id, flow):
        async with self._lock:
            self._active_users_map[user_id] = flow
    
    async def remove_active_user(self, user_id):
        async with self._lock:
            self._active_users_map.pop(user_id, None)
    
    async def add_answered_question(self, user_id, question_id):
        async with self._lock:
            self._answered_questions[user_id].add(question_id)
    
    async def remove_answered_questions(self, user_id):
        async with self._lock:
            self._answered_questions.pop(user_id, None)
    
    async def is_question_answered(self, user_id, question_id):
        async with self._lock:
            return question_id in self._answered_questions[user_id]

# Global thread-safe state instance
state = ThreadSafeState()

# Backward compatibility (deprecated - use state instead)
active_users_map = {}
answered_questions = {}
