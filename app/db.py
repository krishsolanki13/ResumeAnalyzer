# app/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.base import Base  

# SQLite database URL (you can change this to PostgreSQL or MySQL)
DATABASE_URL = "sqlite:///data/resumes.db"

# Set up the database engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
