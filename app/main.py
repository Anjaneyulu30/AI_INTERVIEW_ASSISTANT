from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine

# Import all models
from app.models import User

# Import routers
from app.api.user import router as user_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Interview Assistant",
    version="1.0.0"
)

# Register API routes
app.include_router(user_router)


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Interview Assistant API is running"
    }