from pydantic import BaseModel


class InterviewRequest(BaseModel):
    resume_text: str


class InterviewResponse(BaseModel):
    question: str


class AnswerRequest(BaseModel):
    question: str
    answer: str


class EvaluationResponse(BaseModel):
    score: int
    feedback: str