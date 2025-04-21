# # app/resume_operations.py

# from app.db import SessionLocal  # Import the database session
# from models.resume_model import Resume  # Import the Resume model

# def add_resume_to_db(name, email, contact, github, linkedin, work_experience_summary, projects_summary, skills, ats_evaluation):
#     # Create a database session
#     db = SessionLocal()

#     try:
#         # Create a new instance of the Resume model with the data
#         resume = Resume(
#             name=name,
#             email=email,
#             contact=contact,
#             github=github,
#             linkedin=linkedin,
#             work_experience_summary=work_experience_summary,
#             projects_summary=projects_summary,
#             skills=skills,
#             ats_evaluation=ats_evaluation
#         )

#         # Add the new resume to the session
#         db.add(resume)

#         # Commit the session to save the resume in the database
#         db.commit()
        
#         print("Resume added successfully!")

#     except Exception as e:
#         # Rollback in case of an error
#         print(f"Error adding resume: {e}")
#         db.rollback()

#     finally:
#         # Close the session after the operation
#         db.close()

# # If you need to fetch resumes or perform other operations, you can add them here.


from app.db import SessionLocal
from models.resume_model import Resume
import re
import pandas as pd
import json
import io

def add_resume_to_db(name, email, contact, github, linkedin, work_experience_summary, projects_summary, skills, ats_evaluation):
    db = SessionLocal()
    try:
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
        db.add(resume)
        db.commit()
        print("Resume added successfully!")
    except Exception as e:
        print(f"Error adding resume: {e}")
        db.rollback()
    finally:
        db.close()

def extract_ats_score(ats_text):
    match = re.search(r'(\d+(\.\d+)?)\s*%', ats_text)
    if match:
        return float(match.group(1))
    return None

def query_resumes(name=None, skills=None, ats_score=None, work_experience_role=None):
    db = SessionLocal()
    try:
        query = db.query(Resume)

        if name:
            query = query.filter(Resume.name.ilike(f"%{name}%"))

        if skills:
            query = query.filter(Resume.skills.ilike(f"%{skills}%"))

        if work_experience_role:
            query = query.filter(Resume.work_experience_summary.ilike(f"%{work_experience_role}%"))

        resumes = query.all()

        if ats_score is not None:
            filtered_resumes = []
            for resume in resumes:
                score = extract_ats_score(resume.ats_evaluation)
                if score is not None and score >= ats_score:
                    filtered_resumes.append(resume)
            return filtered_resumes

        return resumes

    except Exception as e:
        print(f"Error querying resumes: {e}")
        return []
    finally:
        db.close()

def convert_resumes_to_csv_bytes(resumes):
    data = [{
        "Name": resume.name,
        "Email": resume.email,
        "Skills": resume.skills,
        "ATS Score": resume.ats_evaluation,
        "Work Experience": resume.work_experience_summary
    } for resume in resumes]

    df = pd.DataFrame(data)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue().encode('utf-8')

def convert_resumes_to_json_bytes(resumes):
    data = [{
        "Name": resume.name,
        "Email": resume.email,
        "Skills": resume.skills,
        "ATS Score": resume.ats_evaluation,
        "Work Experience": resume.work_experience_summary
    } for resume in resumes]

    json_buffer = io.StringIO()
    json.dump(data, json_buffer, indent=4)
    return json_buffer.getvalue().encode('utf-8')
