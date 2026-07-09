from app.database.session import SessionLocal
from app.models.evaluation import Evaluation


def evaluate_answer(question: str, answer: str):

    # Temporary evaluation logic
    # Later we can replace with Gemini
    score = 8

    feedback = (
        "Good answer. "
        "Your explanation is clear. "
        "Try adding more technical details and real project examples."
    )

    # Save evaluation result into database
    db = SessionLocal()

    try:
        evaluation = Evaluation(
            question=question,
            answer=answer,
            score=score,
            feedback=feedback
        )

        db.add(evaluation)
        db.commit()
        db.refresh(evaluation)

    finally:
        db.close()

    return {
        "score": score,
        "feedback": feedback
    }