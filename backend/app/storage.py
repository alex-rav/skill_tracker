import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "skills.json"


def read_skills():
    if not DATA_FILE.exists():
        return[]
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    

def write_skills(skills):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(skills, f, ensure_ascii=False, indent=2)