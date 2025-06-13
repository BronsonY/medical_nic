from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Institute
from schemas import InstituteOut
from database import SessionLocal

router = APIRouter(
    prefix="",
    tags=["Institutes"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[InstituteOut])
def read_institutes(db: Session = Depends(get_db)):
    return db.query(Institute).all()
