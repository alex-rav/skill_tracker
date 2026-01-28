from backend.app.services import get_all_skills, create_skill, delete_skill

print("Текущие навыки:")
print(get_all_skills())

print("\nУдаляем навык с id = 5")
result = delete_skill(5)

print("Результат:", result)
print("Навыки после удаления:")
print(get_all_skills())


