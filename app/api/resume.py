from fastapi import APIRouter, UploadFile, File, Depends

from app.services.resume_service import (
    save_resume,
    extract_text
)

from app.schemas.resume import ResumeResponse
from app.core.security import get_current_user


router = APIRouter()


@router.post(
    "/upload-resume",
    response_model=ResumeResponse
)
async def upload_resume(
    file: UploadFile = File(...),
    current_user = Depends(get_current_user)
):

    file_path = save_resume(file)

    text = extract_text(file_path)

    return {
        "filename": file.filename,
        "text": text
    }