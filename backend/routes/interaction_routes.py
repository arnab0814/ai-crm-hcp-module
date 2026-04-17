from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from services.interaction_service import (
    create_interaction,
    get_all_interactions,
    update_interaction
)

router = APIRouter(prefix="/interactions", tags=["Interactions"])


@router.post("/")
def log_interaction(data: dict, db: Session = Depends(get_db)):
    return create_interaction(db, data)


@router.get("/")
def get_interactions(db: Session = Depends(get_db)):
    return get_all_interactions(db)


@router.put("/{interaction_id}")
def edit_interaction(interaction_id: int, data: dict, db: Session = Depends(get_db)):
    updated = update_interaction(db, interaction_id, data)
    
    if not updated:
        return {"error": "Interaction not found"}
    
    return updated

from services.ai_service import extract_interaction_data
import json

@router.post("/ai-log")
def ai_log_interaction(input_text: dict, db: Session = Depends(get_db)):
    try:
        raw_text = input_text.get("text")

        ai_result = extract_interaction_data(raw_text)

        # 🔥 CLEAN RESPONSE
        cleaned = ai_result.replace("```json", "").replace("```", "").strip()

        parsed = json.loads(cleaned)

        return parsed

    except Exception as e:
        return {"error": str(e)}
    
from agent.langgraph_agent import app as agent_app

@router.post("/agent")
def run_agent(input_text: dict):
    result = agent_app.invoke({"input": input_text.get("text")})
    return result    