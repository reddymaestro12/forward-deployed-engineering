from typing import List

from pydantic import BaseModel, Field

from fastapi import FastAPI

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str = Field(None, title="name of student", max_length=10)
    subjects: List[str] = []


@app.post("/students/")
async def student_data(s1: Student):
    return s1
