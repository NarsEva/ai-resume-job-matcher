from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity_score * 100, 2)


if __name__ == "__main__":
    resume = """
    Java Spring Boot REST API SQL MySQL PostgreSQL AWS Docker Kubernetes
    backend development microservices Git Postman Swagger
    """

    job = """
    We are looking for a Java AI Engineer with experience in Java, Spring Boot,
    REST APIs, AWS, Python, machine learning, and AI tools.
    """

    score = calculate_match_score(resume, job)

    print(f"Match Score: {score}%")