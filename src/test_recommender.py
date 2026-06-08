from src.job_recommender import recommend_jobs


resume = """
Java Spring Boot REST API SQL PostgreSQL AWS Docker Kubernetes
Git Postman Swagger backend development microservices
"""

results = recommend_jobs(resume)

print(results)