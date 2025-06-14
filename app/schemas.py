# app/schemas.py

from pydantic import BaseModel
from typing import Optional, List

class ActivityCreate(BaseModel):
    name: str
    category: Optional[str] = None
    points: Optional[int] = 0

class ActivityOut(ActivityCreate):
    id: int

    class Config:
        orm_mode = True