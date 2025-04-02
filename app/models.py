from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    dob = Column(Date)
    amount_due = Column(Float) 