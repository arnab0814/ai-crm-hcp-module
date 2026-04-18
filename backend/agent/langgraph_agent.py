from langgraph.graph import StateGraph
from services.ai_service import extract_interaction_data
from agent.tools import summarize_interaction_tool, suggest_next_action_tool


# Simple state
from typing import TypedDict
from services.interaction_service import (
    create_interaction,
    get_all_interactions,
    update_interaction
)
from database.db import SessionLocal
import json
class AgentState(TypedDict, total=False):
    input: str
    action: str
    result: dict
    data: dict   # 🔥 ADD THIS
    
def decide_action(state: AgentState):
    user_input = state.get("input", "").lower()

    if "summary" in user_input or "summarize" in user_input:
        return {"action": "summarize"}

    elif "suggest" in user_input or "recommend" in user_input:
        return {"action": "suggest"}

    elif "update" in user_input or "edit" in user_input:
        return {"action": "edit"}

    elif "show" in user_input or "get" in user_input:
        return {"action": "get"}

    else:
        return {"action": "log"}

def handle_action(state: AgentState):
    action = state.get("action")
    user_input = state.get("input")

    db = SessionLocal()

    try:
        if action == "log":
            extracted = extract_interaction_data(user_input)

            cleaned = extracted.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned)

            saved = create_interaction(db, data)
            print("DEBUG RETURN DATA:", data)

            return {
                "input": user_input,
                "action": action,
                "result": f"Interaction saved with ID {saved.id}",
                "data": data   # 🔥 CRITICAL FIX
            }

        elif action == "get":
            data = get_all_interactions(db)

            cleaned = [
            {
                "doctor_name": d.doctor_name,
                "product": d.product,
                "notes": d.notes,
                "follow_up": d.follow_up
            }
            for d in data
            if d.doctor_name is not None
            ]

            return {
                "input": user_input,
                "action": action,
                "result": cleaned
            }

        elif action == "edit":
            # For now assume ID = 1 (you can improve later)
            extracted = extract_interaction_data(user_input)

            cleaned = extracted.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned)

            updated = update_interaction(db, 1, data)

            return {
                "input": user_input,
                "action": action,
                "result": "Interaction updated"
            }
        
        elif action == "summarize":
            extracted = extract_interaction_data(user_input)

            cleaned = extracted.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned)

            summary = summarize_interaction_tool(data)

            return {
                "input": user_input,
                "action": action,
                "result": summary
            }


        elif action == "suggest":
            extracted = extract_interaction_data(user_input)

            cleaned = extracted.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned)

            suggestion = suggest_next_action_tool(data)

            return {
                "input": user_input,
                "action": action,
                "result": suggestion
            }    

    finally:
        db.close()

# Build graph
graph = StateGraph(AgentState)

graph.add_node("decide", decide_action)
graph.add_node("act", handle_action)

graph.set_entry_point("decide")
graph.add_edge("decide", "act")

app = graph.compile()