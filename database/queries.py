from database import db
from _datetime import datetime


# Save or update user's progress in the current flow
def save_user_progress(user_id, active_flow):
    db['users'].update_one(
        {"_id": user_id},
        {"$set": {"active_flow": active_flow, "last_interaction": datetime.utcnow()}},
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


def save_user_completed_flow(user_id, complted_flow):
    data = {"flow_id": complted_flow["flow_id"], "answers": complted_flow["answers"], "last_interaction": datetime.utcnow()}
    db['users'].update_one(
        {"_id": user_id},
        {"$push": {"completed_flows": data}, "$unset": {"active_flow": ""}},
        upsert=True
    )

def get_user_data(user_id):
    return db.users.find_one({"_id": user_id})
