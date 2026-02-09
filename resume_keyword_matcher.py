import streamlit as st

st.title("📄 Resume Keyword Matcher")

resume = st.text_area("Paste Resume Text", height=200)
job_desc = st.text_area("Paste Job Description", height=200)

if st.button("Analyze"):
    if resume and job_desc:
        resume_words = set(resume.lower().split())
        job_words = set(job_desc.lower().split())

        matched = resume_words & job_words
        missing = job_words - resume_words

        st.subheader("Matched Keywords")
        st.write(", ".join(sorted(matched)))

        st.subheader("Missing Keywords")
        st.write(", ".join(sorted(missing)))
    else:
        st.warning("Please fill both fields")
