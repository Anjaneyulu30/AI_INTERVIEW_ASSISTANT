# AI Interview Assistant

An AI-powered interview preparation platform built using FastAPI and Google's Gemini API. The application allows users to register, log in securely, upload resumes, extract resume text, generate interview questions, and evaluate answers.

## Features

- User Registration & Login (JWT Authentication)
- Resume Upload (PDF/DOCX)
- Resume Text Extraction
- AI-Based Interview Question Generation
- AI Answer Evaluation
- Swagger API Documentation
- Modular FastAPI Project Structure

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Google Gemini API
- pdfplumber
- python-docx
- Pydantic
- Uvicorn

## Project Structure

```
app/
 ├── api/
 ├── core/
 ├── database/
 ├── models/
 ├── schemas/
 ├── services/
 ├── uploads/
 └── main.py
```

## Installation

```bash
git clone https://github.com/Anjaneyulu30/AI-Interview-Assistant.git

cd AI-Interview-Assistant

python -m venv nenv21

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

- Register
- Login
- Upload Resume
- Generate Interview Questions
- Evaluate Answers
- Get Current User

## Note

This project uses Google's Gemini API. If the free quota is exhausted, AI-based question generation and evaluation may temporarily be unavailable until the quota resets or a new API key is used.

## Future Improvements

- Multiple Question Generation
- Difficulty Levels
- Resume Skill Analysis
- Mock Interview Session
- Voice-based Interview
- Interview Performance Dashboard

## Author

Badineni Venkata Anjaneyulu