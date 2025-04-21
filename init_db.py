# init_db.py

from app.db import engine  
from app.base import Base  
from models.resume_model import Resume 

# Create all tables in the database
Base.metadata.create_all(bind=engine)

print("Database initialized successfully.")
