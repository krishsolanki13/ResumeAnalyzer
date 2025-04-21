# app/debug_db.py
from app.db import SessionLocal
from models.resume_model import Resume

db = SessionLocal()
resumes = db.query(Resume).all()

for r in resumes:
    # Print all fields of the Resume object dynamically
    for column, value in r.__dict__.items():
        if column != '_sa_instance_state':  # Avoid printing internal SQLAlchemy state
            print(f"{column}: {value}")
    print()  # Adding a new line between records for better readability
