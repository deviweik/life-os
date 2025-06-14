# app/routes/activity_log.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Activity, ActivityLog
from app.schemas import ActivityLogCreate, ActivityLogOut
from typing import List
from datetime import datetime, timezone, timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/activity-logs/", response_model=ActivityLogOut)
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

@router.get("/activity-logs/today-points")
def get_today_total_points(db: Session = Depends(get_db)):
    start, end = get_utc_day_bounds()

    total = (
        db.query(func.sum(Activity.points))
        .join(ActivityLog, Activity.id == ActivityLog.activity_id)
        .filter(ActivityLog.timestamp >= start, ActivityLog.timestamp < end)
        .scalar() or 0
    )

    return {"total_points": total}

def get_utc_day_bounds():
    now = datetime.now(timezone.utc)
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)
    return start_of_day, end_of_day