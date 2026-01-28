from backend.app.storage import read_skills, write_skills
from   backend.app.constants import CATEGORIES


def get_all_skills():
    return read_skills()

# Добавление с проверкой на дубликат

def create_skill(name: str, category: str):
    if category not in CATEGORIES:
        raise ValueError("Invalid category")

    skills = read_skills()

    for skill in skills:
        if skill["name"].lower() == name.lower():
            return None
        
    new_id = max([s["id"] for s in skills], default=0) + 1

    new_skill = {
        "id": new_id,
        "name": name,
        "category": category
    }

    skills.append(new_skill)
    write_skills(skills)

    return new_skill


'''
Добавление навыков без проверки на дубликат

def create_skill(name: str):
    skills = read_skills()

    if skills:
        new_id = max(skill["id"] for skill in skills) + 1
    else:
        new_id = 1

    new_skill = {
        "id": new_id,
        "name": name
    }

    skills.append(new_skill)
    write_skills(skills)

    return new_skill

'''
def delete_skill(skill_id: int) -> bool:
    skills = read_skills()

    filtered_skills = [s for s in skills if s["id"] !=skill_id]

    if len(filtered_skills) == len(skills):
        return False
    
    write_skills(filtered_skills)
    return True


def get_skill_by_category():
    skills = read_skills()
    result = {}

    for skill in skills:
        category = skill["category"]

        if category not in result:
            result[category] = []

        result[category].append(skill)

    return result