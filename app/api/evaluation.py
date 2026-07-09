from fastapi import APIRouter
from app.schemas.evaluation import AnswerRequest, EvaluationResponse
from app.services.evaluation_service import evaluate_answer

router = APIRouter()


@router.post("/evaluate-answer", response_model=EvaluationResponse)
def evaluate(request: AnswerRequest):

    result = evaluate_answer(
        request.question,
        request.answer
    )

    return result