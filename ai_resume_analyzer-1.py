import streamlit as st
import fitz  # PyMuPDF

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    st.subheader("Resume Text")
    st.write(text)

    skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "data science",
        "c++",
        "html",
        "css",
        "javascript",
        "git"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Detected Skills")
    st.write(found_skills)

    score = len(found_skills) * 10

    if score > 100:
        score = 100

    st.subheader("Resume Score")
    st.write(score, "/ 100")

    st.subheader("Suggestions")

    if score < 50:
        st.write("Add more technical skills.")
        st.write("Add projects.")
        st.write("Add certifications.")
    else:
        st.write("Good resume. Keep improving.")