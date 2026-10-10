
from pydantic import BaseModel, Field


class SkillCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    category: str = Field(..., min_length=1, max_length=50)
    proficiency: str = Field(
        ..., pattern="^(Beginner|Intermediate|Advanced)$"
    )
    hours_spent: int = Field(default=0, ge=0)
    target_hours: int = Field(default=10, gt=0)


class SkillResponse(SkillCreate):
    id: int
    user_id: int

    model_config = {"from_attributes": True}