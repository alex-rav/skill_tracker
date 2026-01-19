from storage import read_skills, write_skills


def get_all_skills():
    return read_skills()

# Добавление с проверкой на дубликат

def create_skill(name: str):
    skills = read_skills()

    for skill in skills:
        if skill["name"].lower() == name.lower():
            return None
        
    new_id = max([s["id"] for s in skills], default=0) + 1

    new_skill = {
        "id": new_id,
        "name": name
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