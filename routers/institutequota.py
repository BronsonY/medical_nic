from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import InstituteQuota
from schemas import InstituteQuotaBase, InstituteQuotaOut, InstituteQuotaUpdate, InstituteQuotaCreate
from database import SessionLocal

router = APIRouter(
    prefix="",
    tags=["Institute Quota"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/institute_quota/by_institute/{institute_name}", response_model=List[InstituteQuotaOut])
def get_quotas_by_institute(institute_name: str, db: Session = Depends(get_db)):
    quotas = db.query(InstituteQuota).filter(InstituteQuota.institute_name == institute_name).all()
    if not quotas:
        raise HTTPException(status_code=404, detail="No quotas found for this institute")
    return quotas


@router.post("/institute_quota", response_model=InstituteQuotaOut)
def create_institute_quota(data: InstituteQuotaCreate, db: Session = Depends(get_db)):
    # Check if quota already exists for the same institute + point_roster or some other unique key if needed
    existing = (
        db.query(InstituteQuota)
        .filter(InstituteQuota.quota_id == data.quota_id)
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="Quota ID already exists")

    quota = InstituteQuota(**data.dict())
    db.add(quota)
    db.commit()
    db.refresh(quota)
    return quota


@router.put("/institute_quota/by_institute/{institute_name}", response_model=InstituteQuotaOut)
def update_institute_quota_by_institute(institute_name: str, data: InstituteQuotaUpdate, db: Session = Depends(get_db)):
    quota = db.query(InstituteQuota).filter(InstituteQuota.institute_name == institute_name).first()
    if not quota:
        raise HTTPException(status_code=404, detail="Quota for institute not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(quota, key, value)

    db.commit()
    db.refresh(quota)
    return quota