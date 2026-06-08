# AI Resume-to-Job Matcher

An AI-powered web application that analyzes resumes against job descriptions, identifies skill gaps, recommends matching career opportunities, and provides personalized career development insights.

Built with Python, Scikit-learn, Pandas, Streamlit, and Natural Language Processing (NLP) techniques.

## Live Demo

https://ai-resume-job-matcher-sis6kkarknz5ehtlzb2hhi.streamlit.app/

## Features

### Resume Parsing

- Upload resumes in PDF, DOCX, or TXT format
- Extract resume text automatically
- Preview extracted resume text inside the application
- Paste resume text manually as an alternative to uploading

### Job Matching

- Compare a resume against a job description
- Calculate text similarity using TF-IDF and Cosine Similarity
- Identify matched and missing skills
- Generate a fit summary based on the candidate's match
- Calculate an overall fit score

### Skill Analysis

- Extract skills from resumes and job descriptions
- Normalize skill aliases for better matching
- Calculate skill coverage
- Identify missing skills and skill gaps
- Detect relevant technical skills and technologies

### Job Recommendation Engine

- Compare a resume against multiple job opportunities
- Rank jobs based on similarity and skill coverage
- Display recommended jobs in an interactive Streamlit table
- Show overall fit score, skill coverage, text similarity, matched skills, and missing skills for each recommended role

### Career Coach Insights

- Identify candidate strengths
- Highlight missing skills
- Generate learning recommendations
- Suggest career paths based on profile fit

## Tech Stack

### Programming Language

- Python

### Machine Learning & NLP

- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Text Processing

### Data Processing

- Pandas

### Web Application

- Streamlit

### File Processing

- PyPDF
- python-docx

## Project Structure

```text
ai-resume-job-matcher/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── jobs/
│   │   └── jobs.csv
│   └── resumes/
├── src/
│   ├── career_insights.py
│   ├── file_parser.py
│   ├── job_recommender.py
│   ├── matcher.py
│   ├── skills_config.py
│   └── test_setup.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

### 1. Resume Input

The user uploads a resume in PDF, DOCX, or TXT format, or manually pastes resume text into the application.

### 2. Text Extraction

Resume content is extracted, normalized, and prepared for matching.

### 3. Skill Analysis

The application identifies technical skills using configurable skill aliases and normalization rules.

### 4. Similarity Calculation

The resume and job description are converted into TF-IDF vectors and compared using Cosine Similarity.

### 5. Fit Score Generation

The application combines text similarity and skill coverage to generate an Overall Fit Score.

The formula is:

```python
overall_score = (skill_coverage * 0.7) + (text_similarity * 0.3)
```

Both `skill_coverage` and `text_similarity` are already percentages, so the final score is not multiplied by 100 again.

Example:

```text
Skill Coverage: 100%
Text Similarity: 18.75%
Overall Fit Score: 75.62%
```

### 6. Job Recommendations

The resume is evaluated against multiple job profiles and ranked according to compatibility.

### 7. Career Coaching

The application can generate career insights such as strengths, skill gaps, learning recommendations, and suggested career paths.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd ai-resume-job-matcher
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

macOS or Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app/streamlit_app.py
```

If Streamlit is not available as a direct command, run:

```bash
python -m streamlit run app/streamlit_app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Usage

1. Upload a resume file or paste resume text.
2. Paste the job description into the job description box.
3. Click **Analyze Match**.
4. Review the overall fit score, skill coverage, text similarity, and fit summary.
5. Check the matched and missing skills.
6. Review the recommended jobs table for roles that best match the resume.
7. Use career insights to identify strengths, gaps, and learning priorities.

## Data

Recommended jobs are loaded from:

```text
data/jobs/jobs.csv
```

Each job entry should include a title and description so the recommender can compare the resume against available roles.

## Learning Outcomes

This project demonstrates practical experience with:

- Python development
- Machine Learning fundamentals
- Natural Language Processing
- Recommendation systems
- Data processing with Pandas
- Streamlit application development
- File handling and parsing
- Git and GitHub workflows

## Future Enhancements

- LLM-powered career coaching
- OpenAI integration
- Resume improvement suggestions
- Embedding-based semantic search
- Skill trend analysis
- Interactive analytics dashboard
- Exportable match reports
- Batch resume matching
- Deployment to Streamlit Cloud
- User authentication and profile management

## Author

Nariette Evangelista

Backend Developer transitioning into AI, Machine Learning, and AI Engineering.

## License

This project is for learning and portfolio use.
