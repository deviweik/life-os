# app/schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ActivityCreate(BaseModel):
    name: str
    category: Optional[str] = None
    points: Optional[int] = 0

class ActivityOut(ActivityCreate):
    id: int

    class Config:
        orm_mode = True

class ActivityLogCreate(BaseModel):
    activity_id: int
    timestamp: Optional[datetime] = None

class ActivityLogOut(BaseModel):
    id: int
    activity_id: int
    timestamp: datetime

    class Config:
        orm_mode = True