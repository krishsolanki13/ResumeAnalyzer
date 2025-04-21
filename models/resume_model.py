# #models/resume_model.py

# from sqlalchemy import Column, Integer, String, Text
# from app.base import Base  

# class Resume(Base):
#     __tablename__ = "resumes"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     email = Column(String, nullable=True)
#     contact = Column(String, nullable=True)
#     github = Column(String, nullable=True)
#     linkedin = Column(String, nullable=True)
#     work_experience_summary = Column(Text, nullable=True)
#     projects_summary = Column(Text, nullable=True)
#     skills = Column(Text, nullable=True)
#     ats_evaluation = Column(Text, nullable=True)


#models/resume_model.py

from sqlalchemy import Column, Integer, String, Text
from app.base import Base  

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    contact = Column(String, nullable=True)
    github = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    work_experience_summary = Column(Text, nullable=True)
    projects_summary = Column(Text, nullable=True)
    skills = Column(Text, nullable=True)
    ats_evaluation = Column(Text, nullable=True) 