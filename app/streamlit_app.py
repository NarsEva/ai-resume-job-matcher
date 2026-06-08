import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.career_insights import generate_career_insights
from src.file_parser import extract_text_from_uploaded_file
from src.job_recommender import recommend_jobs
from src.matcher import (
    analyze_skill_match,
    calculate_match_score,
    calculate_overall_fit_score,
    calculate_skill_coverage,
    generate_fit_summary,
)


st.set_page_config(page_title="AI Resume Job Matcher", page_icon="🤖")

st.title("AI Resume-to-Job Matcher")
st.write(
    "Compare your resume against a job description and identify matched and missing skills."
)

uploaded_resume = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])

resume_text = ""

if uploaded_resume is not None:
    resume_text = extract_text_from_uploaded_file(uploaded_resume)
    st.success("Resume uploaded successfully.")

    with st.expander("Preview extracted resume text"):
        st.write(resume_text)
else:
    resume_text = st.text_area("Or paste your resume text here", height=200)

job_description = st.text_area("Paste the job description here", height=200)

if st.button("Analyze Match"):
    if not resume_text.strip() or not job_description.strip():
        st.warning("Please provide both resume text and job description.")
    else:
        score = calculate_match_score(resume_text, job_description)
        matched_skills, missing_skills = analyze_skill_match(
            resume_text,
            job_description,
        )
        coverage = calculate_skill_coverage(matched_skills, missing_skills)
        overall_score = calculate_overall_fit_score(score, coverage)
        summary = generate_fit_summary(overall_score, matched_skills, missing_skills)

        st.metric("Overall Fit Score", f"{overall_score}%")
        st.metric("Skill Coverage", f"{coverage}%")
        st.metric("Text Similarity Score", f"{score}%")

        st.subheader("Fit Summary")
        st.write(summary)

        st.subheader("Matched Skills")
        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.info("No matched skills found.")

        st.subheader("Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("No missing skills found.")

        st.subheader("Recommended Jobs")

        recommendations = recommend_jobs(resume_text)

        display_recommendations = recommendations.rename(
            columns={
                "rank": "Rank",
                "title": "Job Title",
                "overall_score": "Overall Fit Score (%)",
                "skill_coverage": "Skill Coverage (%)",
                "text_similarity": "Text Similarity (%)",
                "matched_skills": "Matched Skills",
                "missing_skills": "Missing Skills",
            }
        )

        display_recommendations["Overall Fit Score (%)"] = display_recommendations[
            "Overall Fit Score (%)"
        ].round(2)

        display_recommendations["Skill Coverage (%)"] = display_recommendations[
            "Skill Coverage (%)"
        ].round(2)

        display_recommendations["Text Similarity (%)"] = display_recommendations[
            "Text Similarity (%)"
        ].round(2)

        st.dataframe(
            display_recommendations,
            column_config={
                "Overall Fit Score (%)": st.column_config.NumberColumn(
                    "Overall Fit Score (%)",
                    format="%.2f%%",
                ),
                "Skill Coverage (%)": st.column_config.NumberColumn(
                    "Skill Coverage (%)",
                    format="%.2f%%",
                ),
                "Text Similarity (%)": st.column_config.NumberColumn(
                    "Text Similarity (%)",
                    format="%.2f%%",
                ),
            },
            hide_index=True,
            use_container_width=True,
        )

        career_insights = generate_career_insights(
            matched_skills,
            missing_skills,
            recommendations,
        )

        st.subheader("Career Coach Insights")

        st.write("**Strengths**")
        if career_insights["strengths"]:
            for strength in career_insights["strengths"]:
                st.success(strength)
        else:
            st.info("No major strengths detected yet.")

        st.write("**Skill Gaps**")
        if career_insights["skill_gaps"]:
            for gap in career_insights["skill_gaps"]:
                st.warning(gap)
        else:
            st.success("No major skill gaps detected.")

        st.write("**Recommended Learning Path**")
        if career_insights["learning_path"]:
            for index, item in enumerate(career_insights["learning_path"], start=1):
                st.write(f"{index}. {item}")
        else:
            st.info("No learning path needed based on detected gaps.")

        st.write("**Suggested Roles**")
        if career_insights["suggested_roles"]:
            for role in career_insights["suggested_roles"]:
                st.write(f"- {role}")