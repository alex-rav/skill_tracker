from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from storage import read_skills, write_skills
from fastapi import HTTPException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Skill(BaseModel):
    name: str

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/skills")
def get_skills():
    return read_skills()

@app.post("/skills")
def add_skill(skill: Skill):
    skills = read_skills()

    if skills:
         
         new_id = max(item.get("id", 0) for item in skills) + 1

    else:

         new_id = 1

    new_skill = {
         "id": new_id,
         "name": skill.name
    }

    skills.append(new_skill)
    write_skills(skills)

    return new_skill

@app.delete("/skills/{skill_id}")
def delete_skill(skill_id: int):
    skills = read_skills()

    filtered_skills = [s for s in skills if s["id"] != skill_id]

    if len(filtered_skills) == len(skills):
            raise HTTPException(status_code=404, detail="Skill not found")
    
    write_skills(filtered_skills)
    return {"status": "deleted"}
            