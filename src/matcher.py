import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.skills_config import SKILL_ALIASES


def calculate_match_score(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity_score * 100, 2)


def extract_skills(text):
    found_skills = set()
    normalized_text = normalize_text(text)

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            normalized_alias = normalize_text(alias)

            if normalized_alias in normalized_text:
                found_skills.add(skill)
                break

    return sorted(list(found_skills))


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


def generate_fit_summary(score, matched_skills, missing_skills):
    if score >= 70:
        fit_level = "Strong fit"
    elif score >= 40:
        fit_level = "Moderate fit"
    else:
        fit_level = "Low fit"

    summary = f"{fit_level}. The candidate matches {len(matched_skills)} required skill(s)."

    if missing_skills:
        summary += f" To improve fit, focus on: {', '.join(missing_skills)}."
    else:
        summary += " No major missing skills were detected."

    return summary


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def calculate_skill_coverage(matched_skills, missing_skills):
    total_required = len(matched_skills) + len(missing_skills)

    if total_required == 0:
        return 0

    coverage = (len(matched_skills) / total_required) * 100

    return round(coverage, 2)


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def calculate_overall_fit_score(match_score, skill_coverage):
    overall_score = (skill_coverage * 0.7) + (match_score * 0.3)
    return round(overall_score, 2)

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
