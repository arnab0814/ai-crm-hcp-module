from services.interaction_service import (
    create_interaction,
    get_all_interactions,
    update_interaction
)

def log_interaction_tool(db, data):
    return create_interaction(db, data)

def edit_interaction_tool(db, interaction_id, data):
    return update_interaction(db, interaction_id, data)

def get_interactions_tool(db):
    return get_all_interactions(db)

def summarize_tool(data):
    return f"Summary: {data}"

def suggest_next_action_tool(data):
    return "Follow up with doctor in 3 days"