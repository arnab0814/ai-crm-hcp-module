from sqlalchemy.orm import Session
from models.interaction_model import Interaction

def create_interaction(db: Session, data: dict):
    interaction = Interaction(**data)
    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction

def get_all_interactions(db: Session):
    return db.query(Interaction).all()

def update_interaction(db: Session, interaction_id: int, data: dict):
    interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    
    if not interaction:
        return None

    for key, value in data.items():
        setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)
    return interaction