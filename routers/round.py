from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Round
from schemas import RoundOut
from database import SessionLocal

router = APIRouter(
    prefix="",
    tags=["Rounds"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[RoundOut])
def read_rounds(db: Session = Depends(get_db)):
    return db.query(Round).all()
