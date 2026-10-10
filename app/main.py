
from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.auth import router as auth_router
from app.routers.skills import router as skills_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Skill Development Tracker API")

app.include_router(auth_router)
app.include_router(skills_router)


@app.get("/")
def home():
    return {"message": "Welcome to Skill Development Tracker API"}