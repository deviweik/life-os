# app/models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    points = Column(Integer, default=0)