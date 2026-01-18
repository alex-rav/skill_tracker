import json
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

DATA_FILE = Path("skills.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Skill(BaseModel):
    name: str

def load_skills():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_skills(skills):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(skills, f, ensure_ascii=False, indent=2)

skills = load_skills()

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/skills")
def get_skills():
    return skills

@app.post("/skills")
def add_skill(skill: Skill):
    new_id = len(skills) + 1
    new_skill = {
        "id": new_id,
        "name": skill.name
    }
    skills.append(new_skill)
    save_skills(skills)
    return new_skill

@app.delete("/skills/{skill_id}")
def delete_skill(skill_id: int):
    global skills
    for skill in skills:
        if skill["id"] == skill_id:
            