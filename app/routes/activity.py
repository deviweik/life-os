# app/routes/activity.py 

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Activity
from app.schemas import ActivityCreate, ActivityOut
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/activities/")
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    db_activity = Activity(name=activity.name, category=activity.category, points=activity.points)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

@router.get("/activities", response_model=list[ActivityOut])
def get_activities(db: Session = Depends(get_db)):
    activities = db.query(Activity).all()
    return activities