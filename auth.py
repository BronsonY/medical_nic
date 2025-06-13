from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from database import SessionLocal
from models import User
from schemas import UserCreate, UserLogin

router = APIRouter()
SECRET = "secretkey"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed = pwd_context.hash(user.password)
    db_user = User(username=user.username, password=hashed, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg": "User registered"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token_data = {
        "sub": db_user.username,
        "role": db_user.role,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(token_data, SECRET, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}