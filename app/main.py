# app/main.py

from fastapi import FastAPI
from app.routes import activity, activity_log
from app.database import engine, Base
from app import models

# Create DB tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(activity.router)
app.include_router(activity_log.router)

@app.get("/")
def root():
    return {"message": "Life OS backend is running!"}