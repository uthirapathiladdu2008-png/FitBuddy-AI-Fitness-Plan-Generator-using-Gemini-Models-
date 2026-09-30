import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def update_workout_plan(original_plan, feedback):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
Update the following workout plan based on the user's feedback.

ORIGINAL PLAN:
{original_plan}

USER FEEDBACK:
{feedback}

Return a revised 7-day plan with the requested changes while keeping it practical and safe.
"""
    return model.generate_content(prompt).text
