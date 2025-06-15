from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Allocation
from schemas import AllocationOut, AllocationCreate, AllocationDetailOut
from database import SessionLocal

router = APIRouter(
    prefix="",
    tags=["Allocations"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[AllocationOut])
def read_allocations(db: Session = Depends(get_db)):
    return db.query(Allocation).all()

@router.post("/", response_model=AllocationOut, status_code=status.HTTP_201_CREATED)
def create_allocation(allocation: AllocationCreate, db: Session = Depends(get_db)):
    db_allocation = Allocation(**allocation.dict())
    db.add(db_allocation)
    db.commit()
    db.refresh(db_allocation)
    return db_allocation

@router.get("/detailed", response_model=List[AllocationDetailOut])
def read_allocations_with_details(db: Session = Depends(get_db)):
    allocations = db.query(Allocation).all()

    result = []
    for alloc in allocations:
        result.append({
            "id": alloc.id,
            "candidate": alloc.candidate.full_name,  # Assuming Candidate model has 'name'
            "course": alloc.course.course_name,        # Assuming Course model has 'name'
            "institute": alloc.course.institute_name,
            "round": alloc.round.round_number,      # Assuming you want round number or another field
            "allocate": alloc.allocate
        })

    return result
