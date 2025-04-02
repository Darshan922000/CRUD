from pydantic import BaseModel
from datetime import date

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    dob: date
    amount_due: float

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class Student(StudentBase):
    student_id: int

    class Config:
        from_attributes = True 