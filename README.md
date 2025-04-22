# InsightCV

InsightCV is a streamlined tool for parsing, analyzing, and evaluating resumes. It extracts personal and professional information from uploaded resumes using a combination of rule-based logic and Gemini LLM. Users can query resumes based on multiple filters and export the filtered data in multiple formats. The system supports multilingual documents and provides ATS-style scoring to enhance decision-making during hiring.

## Features

### Resume Parsing

InsightCV combines two approaches for information extraction:

1. **Rule-based extraction** (using SpaCy and pattern-matching):
   - Name
   - Email address
   - Phone number
   - LinkedIn URL
   - GitHub URL

2. **Gemini LLM-based analysis**:
   - Work experience summary
   - Projects summary
   - Skills summary
   - ATS-style evaluation and score

### Resume Querying

Users can query the parsed resume database using the following parameters:
- Candidate name
- Specific skills
- Minimum ATS score
- Keywords in work experience
- Full database (no filters)

### Data Exporting

Queried data can be exported in:
- JSON format
- CSV format

Exports are saved locally to the user’s device.

### Multilingual Support

InsightCV supports parsing and evaluating resumes written in the following languages:
- English
- Spanish
- French
- German
- Italian

## Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **NLP/AI/LLM**: Gemini LLM, SpaCy  
- **File Parsing**: pdfplumber, python-docx  
- **Database**: SQLite (via SQLAlchemy)  
- **Utilities/Libraries**: Pandas, OS, JSON, CSV  
- **IDE**: Windsurf (Codeium’s AI Agentic IDE)

## Setup Instructions

### Prerequisites
Before running the app, make sure you have the following:

1. **Gemini API Key**: You will need a valid Gemini API key to use the app.
2. **Docker Desktop (if using Docker)**: Make sure Docker Desktop is installed if you plan to run the app using Docker.

### Option 1: Running the App Locally (Without Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/krishsolanki13/ResumeAnalyzer.git
   cd ResumeAnalyzer

2. Create a virtual environment:
   ```bash
   python -m venv venv

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
  
4. Install dependencies:
   ```bash
   pip install -r requirements.txt

5. Create a .env file in the project root directory and add the following line with your Gemini API key
   ```ini
   GEMINI_API_KEY=your_api_key_here

6. Run the application:
   ```bash
   streamlit run frontend/main.py

7. Access the app:
   Open your browser and go to [http://localhost:8501](http://localhost:8501).

### Option 2: Running the App Using Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/krishsolanki13/ResumeAnalyzer.git
   cd ResumeAnalyzer

2. Build the Docker image:
   ```bash
   docker build -t insightcv .

3. Run the application with database persistence:
   ```bash
   docker run -p 8501:8501 -v ${PWD}/data:/app/data -e GEMINI_API_KEY=your_api_key_here insightcv

4. Access the app: 
   Open your browser and go to [http://localhost:8501](http://localhost:8501).

## Folder Structure

```plaintext
InsightCV/
│
├── app/
│   ├── __init__.py
│   ├── extractor.py
│   ├── db.py
│   ├── debug_db.py
│   ├── gemini_analysis.py
│   ├── rule_based_extractor.py
│   ├── resume_operations.py
│   ├── base.py
│   ├── clear_data.py
│   └── utils.py
│
├── frontend/
│   ├── __init__.py
│   ├── main.py
│   ├── upload_section.py
│   └── query_section.py
│
├── data/
│   ├── resumes/
│   ├── resumes.db
│   └── output/
│
├── models/
│   ├── __pycache__/
│   ├── resume_model.py
│
├── venv/
├── .env
├── requirements.txt
├── README.md
├── .gitignore
├── run_app.py
├── test_env.py
├── test_gemini.py
└── init_db.py
```


## Contributors

- **Author**: [Kriish Solanki](https://github.com/krishsolanki13)



