#frontend/main.py

import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'frontend')))
from upload_section import handle_resume_upload
from query_section import show_query_section

# Set up the Streamlit page layout
st.set_page_config(page_title="InsightCV", layout="wide")

# Display a title and description
st.title("InsightCV")
st.write("Upload a resume (PDF or DOCX), and we will extract key information from it.")

# Use session state to keep track of the current page
if 'page' not in st.session_state:
    st.session_state.page = 'upload'  # Default page

# Display either the Upload Section or Query Section based on the session state
if st.session_state.page == 'upload':
    # Call the function to handle resume upload
    extracted_text = handle_resume_upload()

    # Check if any extracted text exists
    if extracted_text:
        st.success("Text extracted successfully!")
    else:
        st.warning("Please upload a valid resume to extract text.")

elif st.session_state.page == 'query':
    show_query_section()
