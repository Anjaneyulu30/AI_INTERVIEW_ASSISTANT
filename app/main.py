from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine

# Import models for database tables
import app.models.user
import app.models.evaluation

# Import routers
from app.api import auth
from app.api import user
from app.api import resume
from app.api import interview
from app.api import evaluation


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Interview Assistant",
    version="1.0.0"
)


# Authentication routes
app.include_router(auth.router)

# User routes
app.include_router(user.router)

# Resume routes
app.include_router(resume.router)

# Interview routes
app.include_router(interview.router)

# Evaluation routes
app.include_router(evaluation.router)


@app.get("/")
def root():
    return {
        "message": "AI Interview Assistant API is running"
    }