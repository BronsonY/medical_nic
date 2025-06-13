from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Course
from schemas import CourseOut
from database import SessionLocal

router = APIRouter(
    prefix="",
    tags=["Courses"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CourseOut])
def read_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()