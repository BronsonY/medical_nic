from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# ============ Institute ============

class InstituteBase(BaseModel):
    institute_name: str
    short_name: Optional[str] = None

class InstituteCreate(InstituteBase):
    pass

class InstituteOut(InstituteBase):
    inst_code: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# ============ Course ============

class CourseBase(BaseModel):
    institute_course_id: int
    institute_name: str
    course_name: str
    year: Optional[int] = None
    inst_short_name: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class CourseOut(CourseBase):
    institute_course_id: int
    institute_name: str
    created_at: datetime
    updated_at: datetime
    inst_short_name: Optional[str] = None

    class Config:
        orm_mode = True

# ============ Candidate ============

class CandidateBase(BaseModel):
    mobile_no: str
    full_name: str
    email: EmailStr
    password: str  # You may exclude in Out if needed
    guardian_full_name: Optional[str] = None
    current_address_line_1: Optional[str] = None
    current_address_line_2: Optional[str] = None
    current_state_code: Optional[str] = None
    current_district_code: Optional[str] = None
    current_pin_code: Optional[str] = None
    domicile_state_code: Optional[str] = None
    domicile_district_code: Optional[str] = None
    caste_category: Optional[str] = None
    special_category: Optional[str] = None
    profile_status: Optional[str] = None
    photo_sign_upload_status: Optional[str] = None
    nta_application_id: int = None
    is_registered: Optional[bool] = False

class CandidateCreate(CandidateBase):
    pass

class CandidateOut(CandidateBase):
    id: int
    date_of_registration: datetime

    class Config:
        orm_mode = True

# ============ Round ============

class RoundBase(BaseModel):
    round_number: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = None

class RoundCreate(RoundBase):
    pass

class RoundOut(RoundBase):
    round_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# ============ Allocation ============

class AllocationBase(BaseModel):
    candidate_id: int
    course_id: int
    round_id: int
    allocate: Optional[bool] = False

class AllocationCreate(BaseModel):
    candidate_id: int
    course_id: int
    round_id: int
    allocate: bool = False  # optional, defaults to False if not provided

class AllocationDetailOut(BaseModel):
    id: int
    candidate: str
    course: str
    round: str
    allocate: bool

    class Config:
        orm_mode = True

class AllocationOut(AllocationBase):
    id: int

    class Config:
        orm_mode = True


# ========= Institute Quota ======================
class InstituteQuotaBase(BaseModel):
    institute_name: str   # match the model's FK field
    exam_name: Optional[int] = None
    total_seats: Optional[int] = None
    ur: Optional[int] = None
    sc: Optional[int] = None
    st: Optional[int] = None
    obc_m: Optional[int] = None
    obc_mp: Optional[int] = None
    obc_tn: Optional[int] = None
    point_roster: Optional[str] = None

class InstituteQuotaCreate(InstituteQuotaBase):
    quota_id: str

class InstituteQuotaUpdate(BaseModel):
    exam_name: Optional[int] = None
    total_seats: Optional[int] = None
    ur: Optional[int] = None
    sc: Optional[int] = None
    st: Optional[int] = None
    obc_m: Optional[int] = None
    obc_mp: Optional[int] = None
    obc_tn: Optional[int] = None
    point_roster: Optional[str] = None

class InstituteQuotaOut(InstituteQuotaBase):
    quota_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True