# app/main.py

from fastapi import FastAPI
from app.routes import activity
from app.database import engine, Base

# Create DB tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(activity.router)

@app.get("/")
def root():
    return {"message": "Life OS backend is running!"}