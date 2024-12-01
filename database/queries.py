from database import db
from _datetime import datetime, timedelta


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
        return user.get('active_flow', {})
    return {}


# Reset user progress when restarting the flow
def reset_user_progress(user_id):
    db.users.update_one(
        {"_id": user_id},
        {"$unset": {"active_flow": ""}}
    )


def save_user_completed_flow(user_id, complted_flow):
    if complted_flow["flow_id"] == "restart_flow": # ignore restart flows and don't save in DB
        db['users'].update_one(
            {"_id": user_id},
            {"$unset": {"active_flow": ""}},
            upsert=True
        )
        return
    data = {"flow_id": complted_flow["flow_id"], "answers": complted_flow["answers"], "last_interaction": datetime.utcnow()}
    db['users'].update_one(
        {"_id": user_id},
        {"$push": {"completed_flows": data}, "$unset": {"active_flow": ""}},
        upsert=True
    )


def get_user_data(user_id):
    return db.users.find_one({"_id": user_id})


def remove_expired_active_flow(user_data):
    # Calculate the time 15 minutes ago
    expiration_time = datetime.utcnow() - timedelta(minutes=0.05)

    # Check if last interaction is older than 15 minutes
    if user_data["last_interaction"] < expiration_time:
        # Update user document to remove active_flow
        db['users'].update_one(
            {"_id": user_data["_id"]},
            {"$unset": {"active_flow": ""}}
        )
        return True
    else:
        return False