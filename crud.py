from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from models import College, User
from schemas import CollegeCreate
from database import SessionLocal

router = APIRouter()
SECRET = "secretkey"
ALGORITHM = "HS256"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")

@router.post("/create")
def create_college(college: CollegeCreate, token: str, db: Session = Depends(get_db)):
    user = get_current_user(token)
    if user["role"] != "super_admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    db_college = College(name=college.name, vacancy=college.vacancy)
    db.add(db_college)
    db.commit()
    return {"msg": "College created"}

@router.get("/list")
def list_colleges(db: Session = Depends(get_db)):
    return db.query(College).all()
