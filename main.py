from fastapi import FastAPI
from dotenv import load_dotenv
from .routes import router

load_dotenv()
app = FastAPI(title="FitBuddy - AI Fitness Plan Generator")
app.include_router(router)
