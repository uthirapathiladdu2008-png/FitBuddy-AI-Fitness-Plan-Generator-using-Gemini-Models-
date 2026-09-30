import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_workout_gemini(age, weight, goal, intensity):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
Create a structured 7-day fitness plan for a user.
Age: {age}
Weight: {weight}
Goal: {goal}
Intensity: {intensity}

For each day include:
- Warm-up
- Main workout with exercises, sets/reps or duration
- Cooldown/recovery

Keep the response clear and structured. Include a note that users should
adapt exercise to their ability and seek qualified professional advice when needed.
"""
    return model.generate_content(prompt).text
