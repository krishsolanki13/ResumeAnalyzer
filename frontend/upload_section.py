# import streamlit as st
# import os
# from app.extractor import extract_text_from_resume
# from app.rule_based_extractor import extract_all_fields

# def handle_resume_upload():
#     st.subheader("Upload Your Resume")

#     uploaded_file = st.file_uploader("Upload a PDF or DOCX resume", type=["pdf", "docx"])

#     if uploaded_file is not None:
#         save_path = os.path.join("data", "resumes", uploaded_file.name)
#         with open(save_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         st.success(f"Uploaded `{uploaded_file.name}` successfully.")

#         try:
#             extracted_text = extract_text_from_resume(save_path)
#             st.text_area("Extracted Resume Text", extracted_text, height=400)

#             fields = extract_all_fields(extracted_text)
#             st.subheader("Extracted Fields (Rule-Based)")
#             st.json(fields)

#             return extracted_text
#         except Exception as e:
#             st.error(f"Error extracting text: {str(e)}")

#     return None



# import streamlit as st
# import os
# from app.extractor import extract_text_from_resume
# from app.rule_based_extractor import extract_all_fields
# from app.gemini_analysis import analyze_resume_with_gemini

# def handle_resume_upload():
#     st.subheader("Upload Your Resume")

#     uploaded_file = st.file_uploader("Upload a PDF or DOCX resume", type=["pdf", "docx"])

#     if uploaded_file is not None:
#         save_path = os.path.join("data", "resumes", uploaded_file.name)
#         with open(save_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         st.success(f"Uploaded `{uploaded_file.name}` successfully.")

#         try:
#             # Extract resume text
#             extracted_text = extract_text_from_resume(save_path)

#             # Display extracted text
#             st.text_area("Extracted Resume Text", extracted_text, height=400)

#             # Rule-based extraction
#             fields = extract_all_fields(extracted_text)
#             st.subheader("Extracted Fields (Rule-Based)")
#             st.json(fields)

#             # Gemini LLM Analysis
#             st.subheader("Gemini LLM Analysis")

#             analysis_results = analyze_resume_with_gemini(extracted_text)

#             for section_title, content in analysis_results.items():
#                 st.markdown(f"### {section_title}")
#                 st.write(content)

#             return extracted_text
#         except Exception as e:
#             st.error(f"Error extracting text: {str(e)}")

#     return None


# import streamlit as st
# import os
# from app.extractor import extract_text_from_resume
# from app.rule_based_extractor import extract_all_fields
# from app.gemini_analysis import analyze_resume_with_gemini

# # Available languages for content extraction
# LANGUAGES = ['English', 'Spanish', 'French', 'German', 'Italian']

# def handle_resume_upload():
#     st.subheader("Upload Your Resume")

#     # Language selection dropdown
#     selected_language = st.selectbox(
#         "Select the language for content extraction:",
#         LANGUAGES,
#         index=0  # Default to English
#     )

#     uploaded_file = st.file_uploader("Upload a PDF or DOCX resume", type=["pdf", "docx"])

#     if uploaded_file is not None:
#         save_path = os.path.join("data", "resumes", uploaded_file.name)
#         with open(save_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         st.success(f"Uploaded `{uploaded_file.name}` successfully.")

#         try:
#             # Extract resume text
#             extracted_text = extract_text_from_resume(save_path)

#             # Display extracted text
#             st.text_area("Extracted Resume Text", extracted_text, height=400)

#             # Rule-based extraction
#             fields = extract_all_fields(extracted_text)
#             st.subheader("Extracted Fields (Rule-Based)")
#             for key, value in fields.items():
#                 st.markdown(f"**{key}:** {value}")

#             # Gemini LLM Analysis (with language passed to the function)
#             st.subheader("Gemini LLM Analysis")

#             # Pass the selected language to the Gemini analysis function
#             analysis_results = analyze_resume_with_gemini(extracted_text, selected_language)

#             for section_title, content in analysis_results.items():
#                 st.markdown(f"### {section_title}")
#                 st.write(content)

#             return extracted_text
#         except Exception as e:
#             st.error(f"Error extracting text: {str(e)}")

#     return None


import streamlit as st
import os

from app.extractor import extract_text_from_resume
from app.rule_based_extractor import extract_all_fields
from app.gemini_analysis import analyze_resume_with_gemini
from app.resume_operations import add_resume_to_db

# Available languages for content extraction
LANGUAGES = ['English', 'Spanish', 'French', 'German', 'Italian']

def handle_resume_upload():
    st.subheader("Upload Your Resume")

    # Language selection dropdown
    selected_language = st.selectbox(
        "Select the language for content extraction:",
        LANGUAGES,
        index=0  # Default to English
    )

    uploaded_file = st.file_uploader("Upload a PDF or DOCX resume", type=["pdf", "docx"])

    if uploaded_file is not None:
        save_path = os.path.join("data", "resumes", uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"Uploaded `{uploaded_file.name}` successfully.")

        try:
            # Extract resume text
            extracted_text = extract_text_from_resume(save_path)
            st.text_area("Extracted Resume Text", extracted_text, height=400)

            # Rule-based extraction
            fields = extract_all_fields(extracted_text)
            st.subheader("Extracted Fields (Rule-Based)")
            for key, value in fields.items():
                st.markdown(f"**{key}:** {value}")

            # Gemini LLM Analysis
            st.subheader("Gemini LLM Analysis")
            analysis_results = analyze_resume_with_gemini(extracted_text, selected_language)

            for section_title, content in analysis_results.items():
                st.markdown(f"### {section_title}")
                st.write(content)

            # Automatically insert into DB without a button
            add_resume_to_db(
                name=fields.get("Name", ""),
                email=fields.get("Email", ""),
                contact=fields.get("Contact", ""),
                github=fields.get("GitHub", ""),
                linkedin=fields.get("LinkedIn", ""),
                work_experience_summary=analysis_results.get("Work Experience Summary", ""),
                projects_summary=analysis_results.get("Projects Summary", ""),
                skills=analysis_results.get("Extracted Skills", ""),
                ats_evaluation=analysis_results.get("ATS Evaluation", "")
            )

            st.success("Resume details saved to the database successfully!")

        except Exception as e:
            st.error(f"Error processing resume: {str(e)}")

