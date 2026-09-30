from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .gemini_generator import generate_workout_gemini
from .gemini_flash_generator import generate_nutrition_tip_with_flash
from .updated_plan import update_workout_plan
from .database import save_user, save_plan, get_plan, update_plan, get_all_users, get_all_plans

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(request: Request, username: str = Form(...), user_id: str = Form(...),
                     age: int = Form(...), weight: str = Form(...),
                     goal: str = Form(...), intensity: str = Form(...)):
    plan = generate_workout_gemini(age, weight, goal, intensity)
    tip = generate_nutrition_tip_with_flash(goal)
    save_user({"username": username, "user_id": user_id, "age": age,
               "weight": weight, "goal": goal, "intensity": intensity})
    save_plan({"user_id": user_id, "original_plan": plan,
               "nutrition_tip": tip})
    return templates.TemplateResponse("result.html", {
        "request": request, "username": username, "user_id": user_id,
        "age": age, "weight": weight, "goal": goal, "intensity": intensity,
        "workout_plan": plan, "nutrition_tip": tip
    })

@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(request: Request, user_id: str = Form(...), feedback: str = Form(...)):
    plan = get_plan(user_id)
    if not plan:
        return HTMLResponse("User plan not found", status_code=404)
    revised = update_workout_plan(plan.original_plan, feedback)
    update_plan(user_id, revised)
    return templates.TemplateResponse("result.html", {
        "request": request, "user_id": user_id,
        "workout_plan": revised, "nutrition_tip": plan.nutrition_tip,
        "updated": True
    })

@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request):
    return templates.TemplateResponse("all_users.html", {
        "request": request, "users": get_all_users(), "plans": get_all_plans()
    })
