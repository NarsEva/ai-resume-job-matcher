LEARNING_PATHS = {
    "Python": [
        "Python Fundamentals",
        "Python OOP",
        "Python for Data Analysis"
    ],
    "Scikit-learn": [
        "Machine Learning Basics",
        "Scikit-learn Classification",
        "Scikit-learn Regression"
    ],
    "Machine Learning": [
        "ML Concepts",
        "Supervised Learning",
        "Model Evaluation"
    ],
    "PyTorch": [
        "PyTorch Fundamentals",
        "Neural Networks",
        "Model Training"
    ],
    "TensorFlow": [
        "TensorFlow Basics",
        "Keras",
        "Deep Learning"
    ]
}


def generate_career_insights(
    matched_skills,
    missing_skills,
    recommended_jobs
):
    strengths = []

    if "Java" in matched_skills:
        strengths.append("Strong Java backend foundation")

    if "AWS" in matched_skills:
        strengths.append("Cloud platform experience")

    if "Docker" in matched_skills:
        strengths.append("Containerization experience")

    if "REST API" in matched_skills:
        strengths.append("API development expertise")

    learning_path = []

    for skill in missing_skills:
        if skill in LEARNING_PATHS:
            learning_path.extend(LEARNING_PATHS[skill])

    learning_path = list(dict.fromkeys(learning_path))

    suggested_roles = recommended_jobs["title"].tolist()

    return {
        "strengths": strengths,
        "skill_gaps": missing_skills,
        "learning_path": learning_path,
        "suggested_roles": suggested_roles
    }