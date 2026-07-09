from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.base import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(Text)
    answer = Column(Text)

    score = Column(Integer)
    feedback = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)