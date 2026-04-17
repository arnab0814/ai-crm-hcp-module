from sqlalchemy import Column, Integer, String, Date
from database.db import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String)
    notes = Column(String)
    product = Column(String)
    date = Column(String)
    follow_up = Column(String)