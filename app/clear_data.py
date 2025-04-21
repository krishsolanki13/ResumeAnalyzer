from app.db import SessionLocal
from models.resume_model import Resume

# Create a new session
db = SessionLocal()

# Delete all records from the Resume table
try:
    db.query(Resume).delete()  # This deletes all rows in the Resume table
    db.commit()  # Commit changes to the database
    print("All data deleted from the Resume table.")
except Exception as e:
    print(f"Error deleting data: {e}")
    db.rollback()  # Rollback in case of an error
finally:
    db.close()  # Close the session
