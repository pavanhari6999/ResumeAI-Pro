from streamlit_option_menu import option_menu
import streamlit as st
from PyPDF2 import PdfReader
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from analyzer import analyze_resume
from ai_analyzer import generate_summary
from project_extractor import extract_projects
from cert_extractor import extract_certifications
from role_predictor import predict_roles
from candidate_extractor import extract_name
from education_extractor import extract_education
from experience_extractor import detect_experience
from keyword_gap import keyword_gap
from ats_engine import calculate_ats
from job_matcher import calculate_match
from career_advisor import recommend
from report_generator import generate_report
from recommendation_engine import generate_recommendations

st.set_page_config(
    page_title="ResumeAI Pro",
    page_icon="🚀",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    page = option_menu(
        menu_title="🚀 ResumeAI Pro",
        options=[
            "Dashboard",
            "Resume Analysis",
            "Job Matching",
            "Career Advisor"
        ],
        icons=[
            "house-fill",
            "file-earmark-person-fill",
            "bullseye",
            "briefcase-fill"
        ],
        menu_icon="rocket-takeoff",
        default_index=0
    )

if page == "Dashboard":
    st.markdown("""
    <div class="hero">
        <h1 class="glow">🚀 ResumeAI Pro</h1>
        <div class="hero-subtitle">AI Powered Resume Intelligence Platform</div>
        <br>
        <p style="color:white;font-size:20px;">Analyze • Optimize • Get Hired</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">96%</div>
            <div class="metric-title">ATS Accuracy</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">500+</div>
            <div class="metric-title">Skills Database</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">50+</div>
            <div class="metric-title">Career Roles</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">24/7</div>
            <div class="metric-title">Resume Insights</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("## 📊 Platform Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">12,500+</div>
            <div class="metric-title">Resumes Analyzed</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">150+</div>
            <div class="metric-title">Hiring Partners</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">94%</div>
            <div class="metric-title">Success Rate</div>
        </div>
        """, unsafe_allow_html=True)

elif page == "Resume Analysis":
    st.title("📄 Resume Analysis")

    uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

    if uploaded_file:
        pdf = PdfReader(uploaded_file)
        text = ""
        for pg in pdf.pages:
            page_text = pg.extract_text()
            if page_text:
                text += page_text

        skills, score, suggestions, certifications, projects = analyze_resume(text)
        summary = generate_summary(text)
        projects_found = extract_projects(text)
        certs_found = extract_certifications(text)
        roles_found = predict_roles(skills)
        candidate_name = extract_name(text)
        education = extract_education(text)
        experience = detect_experience(text)
        missing_keywords = keyword_gap(skills)
        dynamic_recommendations = generate_recommendations(
            skills,
            missing_keywords,
            roles_found,
            certifications
        )
        score, breakdown = calculate_ats(
            skills,
            len(projects_found),
            len(certs_found),
            education,
            experience,
            missing_keywords
        )

        st.subheader("👤 Candidate Profile")
        st.success(f"Candidate Name: {candidate_name}")

        st.subheader("🎓 Education")
        if education:
            for item in education:
                st.success(item)
        else:
            st.warning("Education Not Detected")

        st.subheader("💼 Experience Indicator")
        st.metric("Years Mentioned", experience)

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("ATS Score", score)
        col2.metric("Skills", len(skills))
        col3.metric("Certifications", certifications)
        col4.metric("Projects", projects)
        col5.metric("Recommendations", len(dynamic_recommendations))

        st.subheader("📊 ATS Breakdown")
        for section, value in breakdown.items():
            st.write(f"**{section}** : {value}")
            st.progress(min(value / 30, 1.0))

        st.divider()

        st.subheader("🤖 AI Resume Summary")
        st.info(summary)

        left, right = st.columns(2)

        with left:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={"text": "ATS Score"},
                gauge={"axis": {"range": [0, 100]}}
            ))
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("Resume Strength")
            st.progress(score / 100)

            if score >= 80:
                st.success("Excellent Resume")
            elif score >= 60:
                st.warning("Good Resume")
            else:
                st.error("Needs Improvement")

        with right:
            st.subheader("Detected Skills")
            for skill in skills:
                st.success(skill)

        st.subheader("🧠 AI Recommendations")
        for item in dynamic_recommendations:
            st.success(item)

        st.subheader("🔍 Keyword Gap Analysis")
        for keyword in missing_keywords:
            st.warning(f"Missing Skill: {keyword}")

        st.subheader("🚀 Projects Found")
        if projects_found:
            for project in projects_found:
                st.success(project)
        else:
            st.warning("No Projects Detected")

        st.subheader("🏆 Certifications Found")
        if certs_found:
            for cert in certs_found:
                st.success(cert)
        else:
            st.warning("No Certifications Found")

        st.subheader("🎯 AI Predicted Roles")
        if roles_found:
            for role, confidence in roles_found:
                st.success(f"{role} ({confidence}%)")
        else:
            st.warning("No Suitable Roles Predicted")

        if len(skills) > 0:
            chart_df = pd.DataFrame({
                "Skill": skills,
                "Value": [1] * len(skills)
            })
            fig2 = px.pie(
                chart_df,
                names="Skill",
                values="Value",
                title="Skill Distribution"
            )
            st.plotly_chart(fig2, use_container_width=True)

        if st.button("Generate PDF Report"):
            generate_report(
                "resume_report.pdf",
                candidate_name,
                score,
                skills,
                education,
                experience,
                projects_found,
                certs_found,
                roles_found,
                dynamic_recommendations
            )
            with open("resume_report.pdf", "rb") as pdf_file:
                st.download_button(
                    "📥 Download Report",
                    pdf_file,
                    file_name="ResumeAI_Report.pdf",
                    mime="application/pdf"
                )

elif page == "Job Matching":
    st.title("🎯 Job Matching")

    uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
    jd_text = st.text_area("Paste Job Description")

    if uploaded_file and jd_text:
        pdf = PdfReader(uploaded_file)
        resume_text = ""
        for pg in pdf.pages:
            page_text = pg.extract_text()
            if page_text:
                resume_text += page_text

        match_score, missing = calculate_match(resume_text, jd_text)

        st.metric("Match Percentage", f"{match_score}%")

        st.subheader("Missing Keywords")
        for item in missing:
            st.warning(item)

elif page == "Career Advisor":
    st.title("💼 Career Advisor")

    uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

    if uploaded_file:
        pdf = PdfReader(uploaded_file)
        text = ""
        for pg in pdf.pages:
            page_text = pg.extract_text()
            if page_text:
                text += page_text

        skills, score, suggestions, certifications, projects = analyze_resume(text)
        roles = recommend(skills)

        salary_map = {
            "AI Engineer": "8-20 LPA",
            "Cloud Engineer": "6-18 LPA",
            "Blockchain Developer": "8-22 LPA",
            "Frontend Developer": "5-15 LPA",
            "Backend Developer": "6-18 LPA"
        }

        for role in roles:
            st.success(f"{role} | Expected Salary: {salary_map.get(role, 'N/A')}")

        st.info("""
        1. Strengthen Python
        2. Learn Cloud Technologies
        3. Master Git & GitHub
        4. Build Real Projects
        5. Prepare for Interviews
        """)