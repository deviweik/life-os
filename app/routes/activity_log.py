# app/routes/activity_log.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ActivityLog
from app.schemas import ActivityLogCreate, ActivityLogOut
from typing import List
from datetime import datetime, timezone

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/activity_logs/", response_model=ActivityLogOut)
def create_activity_log(log: ActivityLogCreate, db: Session = Depends(get_db)):
    if log.timestamp is None:
        log.timestamp = datetime.now(timezone.utc)
    
    db_activity_log = ActivityLog(
        activity_id=log.activity_id,
        timestamp=log.timestamp
    )
    
    db.add(db_activity_log)
    db.commit()
    db.refresh(db_activity_log)
    return db_activity_log