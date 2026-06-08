from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SKILLS = [
    "Java", "Spring Boot", "REST API", "SQL", "MySQL", "PostgreSQL",
    "AWS", "Docker", "Kubernetes", "Git", "Postman", "Swagger",
    "Python", "Machine Learning", "AI", "Pandas", "NumPy",
    "Scikit-learn", "PyTorch", "TensorFlow", "Streamlit"
]


def calculate_match_score(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity_score * 100, 2)


def extract_skills(text):
    found_skills = []

    text_lower = text.lower()

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


def analyze_skill_match(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    resume = read_text_file("data/resumes/sample_resume.txt")
    job = read_text_file("data/jobs/sample_job.txt")

    score = calculate_match_score(resume, job)
    matched_skills, missing_skills = analyze_skill_match(resume, job)

    print(f"Match Score: {score}%")
    print("\nMatched Skills:")
    for skill in matched_skills:
        print(f"- {skill}")

    print("\nMissing Skills:")
    for skill in missing_skills:
        print(f"- {skill}")