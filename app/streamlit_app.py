import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.matcher import calculate_match_score, analyze_skill_match


st.set_page_config(page_title="AI Resume Job Matcher", page_icon="🤖")

st.title("AI Resume-to-Job Matcher")
st.write("Compare your resume against a job description and identify matched and missing skills.")

resume_text = st.text_area("Paste your resume text here", height=200)
job_description = st.text_area("Paste the job description here", height=200)

if st.button("Analyze Match"):
    if not resume_text.strip() or not job_description.strip():
        st.warning("Please provide both resume text and job description.")
    else:
        score = calculate_match_score(resume_text, job_description)
        matched_skills, missing_skills = analyze_skill_match(resume_text, job_description)

        st.metric("Match Score", f"{score}%")

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