from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_service import generate_interview_question

router = APIRouter()


class InterviewRequest(BaseModel):
    resume_text: str


@router.post("/generate-question")
def generate_question(request: InterviewRequest):
    question = generate_interview_question(request.resume_text)

    return {
        "question": question
    }