from pydantic import BaseModel


class AnswerRequest(BaseModel):
    question: str
    answer: str


class EvaluationResponse(BaseModel):
    score: int
    feedback: str