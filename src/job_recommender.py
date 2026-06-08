import pandas as pd

from src.matcher import (
    calculate_match_score,
    analyze_skill_match,
    calculate_skill_coverage,
    calculate_overall_fit_score
)


def recommend_jobs(resume_text, jobs_csv_path="data/jobs/jobs.csv", top_n=5):
    jobs_df = pd.read_csv(jobs_csv_path)

    recommendations = []

    for _, row in jobs_df.iterrows():
        title = row["title"]
        description = row["description"]

        text_similarity = calculate_match_score(resume_text, description)
        matched_skills, missing_skills = analyze_skill_match(resume_text, description)
        skill_coverage = calculate_skill_coverage(matched_skills, missing_skills)
        overall_score = calculate_overall_fit_score(text_similarity, skill_coverage)

        recommendations.append({
            "title": title,
            "overall_score": overall_score,
            "skill_coverage": skill_coverage,
            "text_similarity": text_similarity,
            "matched_skills": ", ".join(matched_skills),
            "missing_skills": ", ".join(missing_skills)
        })

    recommendations_df = pd.DataFrame(recommendations)

    recommendations_df = recommendations_df.sort_values(
        by="overall_score",
        ascending=False
    ).reset_index(drop=True)

    recommendations_df.insert(
        0,
        "rank",
        range(1, len(recommendations_df) + 1)
    )

    return recommendations_df.head(top_n)