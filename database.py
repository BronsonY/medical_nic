from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Example PostgreSQL URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Temp1234!@localhost:5432/nursing"

# Example filled in:
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/college"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()