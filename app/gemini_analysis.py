# app/gemini_analysis.py

import google.generativeai as genai
from app import utils

genai.configure(api_key=utils.GEMINI_API_KEY)

# Default prompts
WORK_EXP_PROMPT = "Summarize the candidate's work experience from this resume."
PROJECTS_PROMPT = "Summarize the candidate's projects from this resume."
SKILLS_PROMPT = "List the technical and soft skills mentioned in the resume."
ATS_SCORE_PROMPT = """
You are an ATS (Applicant Tracking System) expert. Analyze the resume and give:
1. ATS Match Percentage (out of 100)
2. Final thoughts on resume quality
"""

# Function to append selected language to the prompt
def adapt_prompt_for_language(prompt, language):
    return f"{prompt} in {language}"

def analyze_resume_with_gemini(extracted_text: str, language: str):
    model = genai.GenerativeModel("gemini-1.5-flash")

    def query(prompt):
        # Add the selected language to the prompt
        prompt_in_selected_language = adapt_prompt_for_language(prompt, language)
        response = model.generate_content([prompt_in_selected_language, extracted_text])
        return response.text.strip()

    return {
        "Work Experience Summary": query(WORK_EXP_PROMPT),
        "Projects Summary": query(PROJECTS_PROMPT),
        "Extracted Skills": query(SKILLS_PROMPT),
        "ATS Evaluation": query(ATS_SCORE_PROMPT)
    }
