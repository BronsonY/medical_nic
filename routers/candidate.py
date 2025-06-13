from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Candidate
from schemas import CandidateOut
from database import SessionLocal

router = APIRouter(
    prefix="",
    tags=["Candidates"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CandidateOut])
def read_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).all()
