from services.report_generator import generate_report
from database.database import save_prediction
import streamlit as st

from models.prediction import predict_student

from services.risk_analysis import calculate_risk
from services.weak_area_detector import analyze_performance
from services.suggestions import generate_suggestions
from services.career_guidance import recommend_careers
from services.study_planner import generate_study_plan
from services.academic_health_score import calculate_health_score
from services.explainable_ai import get_feature_importance
from services.ai_advisor import academic_advisor

st.set_page_config(
    page_title="Prediction",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Student Performance Prediction")

st.markdown("---")

# ======================
# STUDENT DETAILS
# ======================

col1, col2 = st.columns(2)

with col1:
    student_name = st.text_input(
        "Student Name"
    )

    cgpa = st.number_input(
        "CGPA (0-10)",
        min_value=0.0,
        max_value=10.0,
        value=8.0
    )

    attendance = st.number_input(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=80
    )

    internal_marks = st.number_input(
        "Internal Marks (0-100)",
        min_value=0,
        max_value=100,
        value=70
    )

    study_hours = st.number_input(
        "Study Hours Per Day",
        min_value=0,
        max_value=12,
        value=4
    )
    
    skills_score = st.number_input(
        "Skills Score (0-10)",
        min_value=0,
        max_value=10,
        value=7
    )

with col2:

    email = st.text_input(
        "Email"
    )

    projects = st.number_input(
        "Projects Completed",
        min_value=0,
        max_value=20,
        value=2
    )

    assignments_completed = st.number_input(
        "Assignments Completed",
        min_value=0,
        max_value=20,
        value=10
    )

    extracurricular_score = st.number_input(
        "Extracurricular Score (0-10)",
        min_value=0,
        max_value=10,
        value=5
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0,
        max_value=12,
        value=7
    )

    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=20,
        value=0
    )

    

# ======================
# BUTTON
# ======================

if st.button(
    "🚀 Predict Performance",
    use_container_width=True
):

    prediction, confidence = predict_student(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        projects,
        assignments_completed,
        extracurricular_score,
        sleep_hours,
        backlogs,
        skills_score
    )

    risk_score, risk_level, reasons = calculate_risk(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        backlogs
    )

    strong_areas, weak_areas = analyze_performance(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        projects,
        skills_score
    )

    suggestions = generate_suggestions(
        attendance,
        internal_marks,
        study_hours,
        projects,
        backlogs,
        skills_score
    )

    careers = recommend_careers(
        cgpa,
        projects,
        skills_score,
        extracurricular_score
    )

    study_plan = generate_study_plan(
        attendance,
        internal_marks,
        study_hours,
        backlogs,
        skills_score
    )

    health = calculate_health_score(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        projects,
        backlogs,
        skills_score
    )

    advisor = academic_advisor(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        backlogs
    )

    feature_importance = get_feature_importance()

    st.markdown("---")

    # ======================
    # TOP METRICS
    # ======================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Prediction",
            prediction.upper()
        )

    with c2:
        st.metric(
            "Confidence",
            f"{confidence}%"
        )

    with c3:
        st.metric(
            "Risk Score",
            risk_score
        )

    with c4:
        st.metric(
            "Health Score",
            health["overall_score"]
        )

    # ======================
    # TABS
    # ======================

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📊 Analysis",
            "💼 Careers",
            "📅 Study Plan",
            "🤖 AI Advisor",
            "📈 Explainable AI"
        ]
    )

    # ======================
    # ANALYSIS
    # ======================

    with tab1:

        col_a, col_b = st.columns(2)

        with col_a:
            st.subheader(
                "✅ Strong Areas"
            )

            for area in strong_areas:
                st.success(area)

        with col_b:
            st.subheader(
                "⚠ Weak Areas"
            )

            for area in weak_areas:
                st.warning(area)

        st.subheader(
            "Improvement Suggestions"
        )

        for suggestion in suggestions:
            st.info(suggestion)

    # ======================
    # CAREERS
    # ======================

    with tab2:

        st.subheader(
            "Recommended Careers"
        )

        for career, score in careers:

            st.write(
                f"**{career}**"
            )

            st.progress(
                score / 100
            )

            st.write(
                f"{score}% Match"
            )

    # ======================
    # STUDY PLAN
    # ======================

    with tab3:

        for day, tasks in study_plan.items():

            with st.expander(day):

                if tasks:

                    for task in tasks:
                        st.write(
                            f"• {task}"
                        )

                else:
                    st.write(
                        "Revision / Free Day"
                    )

    # ======================
    # AI ADVISOR
    # ======================

    with tab4:

        st.subheader(
            "Academic Advisor"
        )

        for advice in advisor:
            st.info(advice)

    # ======================
    # EXPLAINABLE AI
    # ======================

    with tab5:

        st.subheader(
            "Feature Importance"
        )

        for feature, score in feature_importance:

            st.write(
                f"{feature}"
            )

            st.progress(
                min(score / 100, 1.0)
            )

            st.write(
                f"{score}%"
            )

    st.success(
        "Prediction Completed Successfully!"
    )
        # ======================
    # SAVE TO DATABASE
    # ======================

    save_prediction(
        email,
        prediction,
        confidence,
        risk_score,
        risk_level
    )

    # ======================
    # PDF REPORT
    # ======================

    report_path = generate_report(
        student_name,
        prediction,
        confidence,
        risk_score,
        risk_level,
        strong_areas,
        weak_areas,
        suggestions,
        careers
    )

    st.success(
        "📄 PDF Report Generated Successfully!"
    )

    with open(report_path, "rb") as file:

        st.download_button(
            label="📄 Download Report",
            data=file,
            file_name=f"{student_name}_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )