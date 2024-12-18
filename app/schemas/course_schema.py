from typing import List, Optional
from pydantic import BaseModel


class LessonSchema(BaseModel):
    id: str
    title: str
    videoUrl: str
    duration: str
    isFree: bool
    resources: dict
    problemIds: List[str] = []


class ModuleSchema(BaseModel):
    id: str
    title: str
    isFree: bool
    order: int
    description: str
    lessons: List[LessonSchema]


class CourseSchema(BaseModel):
    dsa: Optional[dict] = None
    python: Optional[dict] = None

    class Config:
        orm_mode = True
