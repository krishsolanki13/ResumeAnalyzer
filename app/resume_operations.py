# app/resume_operations.py

from app.db import SessionLocal  # Import the database session
from models.resume_model import Resume  # Import the Resume model

def add_resume_to_db(name, email, contact, github, linkedin, work_experience_summary, projects_summary, skills, ats_evaluation):
    # Create a database session
    db = SessionLocal()

    try:
        # Create a new instance of the Resume model with the data
        resume = Resume(
            name=name,
            email=email,
            contact=contact,
            github=github,
            linkedin=linkedin,
            work_experience_summary=work_experience_summary,
            projects_summary=projects_summary,
            skills=skills,
            ats_evaluation=ats_evaluation
        )

        # Add the new resume to the session
        db.add(resume)

        # Commit the session to save the resume in the database
        db.commit()
        
        print("Resume added successfully!")

    except Exception as e:
        # Rollback in case of an error
        print(f"Error adding resume: {e}")
        db.rollback()

    finally:
        # Close the session after the operation
        db.close()

# If you need to fetch resumes or perform other operations, you can add them here.
