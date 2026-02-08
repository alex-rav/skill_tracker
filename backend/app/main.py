import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.app.services import get_all_skills, create_skill, delete_skill, get_skill_by_category

app = FastAPI()

# Абсолютный путь к папке frontend
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
frontend_path = os.path.join(project_root, "frontend")

app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SkillCreate(BaseModel):
    name: str
    category: str

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/skills")
def get_skills():
    return get_all_skills()

@app.get("/skills/by-category")
def skills_by_category():
    return get_skill_by_category()


@app.post("/skills")
def add_skill(skill: SkillCreate):
    try:
        created = create_skill(skill.name, skill.category)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    if created is None:
        raise HTTPException(
            status_code=400,
            detail="Skill already exists"
        )
    return created


@app.delete("/skills/{skill_id}")
def remove_skill(skill_id: int):
    success = delete_skill(skill_id)
    if not success:
        raise HTTPException(status_code=404, detail="Skill not found")
    return {"status": "deleted"}