from google import genai

from app.core.settings import settings


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def generate_interview_question(resume_text: str) -> str:

    prompt = f"""
You are a senior technical interviewer.

Read the resume and ask ONE realistic interview question.

Rules:
- Ask only one question.
- Make it like a real interviewer.
- Focus on projects and skills.
- Do not give answers.

Resume:
{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text