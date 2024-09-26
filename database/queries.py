from database import db

# Save or update user's progress in the current flow
def save_user_progress(user_id, active_flow):
    db['users'].update_one(
        {"_id": user_id},
        {"$set": {"active_flow": active_flow}},
        upsert=True
    )

# Get user progress in the current flow
def get_user_progress(user_id):
    user = db.users.find_one({"_id": user_id})
    if user:
        return user.get('active_flow', None)
    return None

# Reset user progress when restarting the flow
def reset_user_progress(user_id):
    db.users.update_one(
        {"_id": user_id},
        {"$unset": {"active_flow": ""}}
    )
