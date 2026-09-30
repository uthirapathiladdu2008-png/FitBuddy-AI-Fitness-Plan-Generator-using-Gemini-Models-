# FitBuddy – AI Fitness Plan Generator

## Features
- Personalized 7-day workout plan
- Gemini-powered nutrition/recovery tip
- Feedback-based plan update
- SQLite + SQLAlchemy storage
- FastAPI backend
- Jinja2 HTML frontend
- Admin user view

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your Gemini API key.
4. Run:
   `uvicorn app.main:app --reload`
5. Open `http://127.0.0.1:8000`
6. API docs: `http://127.0.0.1:8000/docs`
