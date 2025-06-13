from sqlalchemy import (
    BigInteger, Column, Integer, String, ForeignKey, DateTime, Boolean
)
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Institute(Base):
    __tablename__ = "institute_master"
    
    inst_code = Column(String, primary_key=True)
    institute_name = Column(String, unique=True, nullable=False)
    short_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    courses = relationship("Course", back_populates="institute")


class Course(Base):
    __tablename__ = "institute_courses"
    
    institute_course_id = Column(Integer, primary_key=True)
    institute_name = Column(Integer, ForeignKey("institute_master.inst_code"), nullable=False)
    course_name = Column(String, nullable=False)
    year = Column(BigInteger)
    inst_short_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    institute = relationship("Institute", back_populates="courses")
    allocations = relationship("Allocation", back_populates="course")


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)
    mobile_no = Column(String(15), nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    date_of_registration = Column(DateTime, default=datetime.utcnow)
    guardian_full_name = Column(String, nullable=True)
    current_address_line_1 = Column(String, nullable=True)
    current_address_line_2 = Column(String, nullable=True)
    current_state_code = Column(String, nullable=True)
    current_district_code = Column(String, nullable=True)
    current_pin_code = Column(String, nullable=True)
    domicile_state_code = Column(String, nullable=True)
    domicile_district_code = Column(String, nullable=True)
    caste_category = Column(String, nullable=True)
    special_category = Column(String, nullable=True)
    profile_status = Column(String, nullable=True)
    photo_sign_upload_status = Column(String, nullable=True)
    nta_application_id = Column(BigInteger, nullable=True)
    is_registered = Column(Boolean, default=False)

    # Relationships
    allocations = relationship("Allocation", back_populates="candidate")


class Round(Base):
    __tablename__ = "round"

    round_id = Column(Integer, primary_key=True)
    round_number = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    allocations = relationship("Allocation", back_populates="round")


class Allocation(Base):
    __tablename__ = "allocations"

    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("institute_courses.institute_course_id"), nullable=False)
    round_id = Column(Integer, ForeignKey("round.round_id"), nullable=False)
    allocate = Column(Boolean, default=False)

    # Relationships
    candidate = relationship("Candidate", back_populates="allocations")
    course = relationship("Course", back_populates="allocations")
    round = relationship("Round", back_populates="allocations")
