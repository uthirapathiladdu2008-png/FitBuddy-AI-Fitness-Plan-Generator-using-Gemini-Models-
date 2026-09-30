import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_nutrition_tip_with_flash(goal):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Give one concise general nutrition or recovery tip for the fitness goal: {goal}. Avoid medical claims."
    return model.generate_content(prompt).text
