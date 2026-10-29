from typing import List

from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(None, description="student name", max_lentgh=10)
    id: int
    subjects: List[str] = []


data = {
    "id": 1,
    "name": "Ravikumar Sharma",
    "subjects": ["Eng", "Maths", "Sci"],
}

student = Student(**data)
print(student)
