# app/debug_db.py
from app.db import SessionLocal
from models.resume_model import Resume

db = SessionLocal()
resumes = db.query(Resume).all()

for r in resumes:
    print(f"Name: {r.name}, Email: {r.email}, Skills: {r.skills}")
