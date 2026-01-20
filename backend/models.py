from pydantic import BaseModel


class Skill(BaseModel):
    id: int
    name: str
    category: str