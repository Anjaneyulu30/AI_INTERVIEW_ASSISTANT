from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine

# Import all models
from app.models import User

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Interview Assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Interview Assistant API is running"
    }