import streamlit as st
from app.resume_operations import query_resumes
import pandas as pd
import json
from io import StringIO, BytesIO

def show_query_section():
    st.title("Query Resumes")
    
    # Move the Back button to the top
    if st.button("Back to Upload Page"):
        st.session_state.page = 'upload'
        st.rerun()

    # Input filters
    name = st.text_input("Candidate Name")
    skills = st.text_input("Skills")
    ats_score = st.number_input("Minimum ATS Score", min_value=0.0, max_value=100.0, step=1.0, format="%.1f")
    work_experience = st.text_input("Work Experience (Role/Keyword)")

    if st.button("Run Query"):
        if not name and not skills and not work_experience and ats_score == 0.0:
            resumes = query_resumes()  # All resumes if no filter
        else:
            # Only send non-empty filters
            resumes = query_resumes(
                name=name if name else None,
                skills=skills if skills else None,
                ats_score=ats_score if ats_score > 0 else None,
                work_experience_role=work_experience if work_experience else None
            )

        if not resumes:
            st.warning("No resumes found matching the criteria.")
            return

        # Show results in a table
        st.subheader("Matching Resumes")
        df = pd.DataFrame([{
            "Name": r.name,
            "Email": r.email,
            "Contact": r.contact,
            "LinkedIn": r.linkedin,
            "GitHub": r.github,
            "Work Experience Summary": r.work_experience_summary,
            "Projects Summary": r.projects_summary,
            "Skills": r.skills,
            "ATS Score": r.ats_evaluation
        } for r in resumes])
        
        # Display the table
        st.dataframe(df)

        # Export CSV
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="Download CSV",
            data=csv_buffer.getvalue(),
            file_name="query_results.csv",
            mime="text/csv"
        )

        # Export JSON
        json_buffer = BytesIO()
        json_data = df.to_dict(orient='records')
        json_str = json.dumps(json_data, indent=4)
        json_buffer.write(json_str.encode())
        json_buffer.seek(0)
        st.download_button(
            label="Download JSON",
            data=json_buffer,
            file_name="query_results.json",
            mime="application/json"
        )
