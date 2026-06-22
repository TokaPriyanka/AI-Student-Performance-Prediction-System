from models.prediction import predict_student

from services.risk_analysis import calculate_risk
from services.weak_area_detector import analyze_performance
from services.suggestions import generate_suggestions
from services.career_guidance import recommend_careers
from services.study_planner import generate_study_plan
from services.academic_health_score import calculate_health_score
from services.explainable_ai import get_feature_importance
from services.ai_advisor import academic_advisor

from services.report_generator import generate_report

from database.database import (
    create_tables,
    add_student,
    save_prediction
)

from utils.helper import (
    print_section,
    display_risk_factors,
    display_areas,
    display_suggestions,
    display_careers,
    display_study_plan,
    display_health_score,
    display_feature_importance
)

from utils.validators import validate_student_data


def main():

    create_tables()

    print_section("AI STUDENT PERFORMANCE SYSTEM")

    student_name = input("Enter Student Name: ")
    student_email = input("Enter Student Email: ")
    cgpa = float(input("CGPA (out of 10): "))
    attendance = int(input("Attendance (0-100%): "))
    internal_marks = int(input("Internal Marks (out of 100): "))
    study_hours = int(input("Study Hours Per Day (0-8 recommended): "))
    projects = int(input("Projects Completed (0-10): "))
    assignments_completed = int(input("Assignments Completed (0-20): "))
    extracurricular_score = int(input("Extracurricular Score (0-10): "))
    sleep_hours = int(input("Sleep Hours Per Day (0-12): "))
    backlogs = int(input("Number of Backlogs: "))
    skills_score = int(input("Technical Skills Score (0-10): "))

    

    valid = validate_student_data(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        projects,
        backlogs,
        skills_score
    )

    if not valid:
        print("\nInvalid Input Data")
        return

    # ---------------------------
    # Prediction
    # ---------------------------

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

    print_section("PERFORMANCE PREDICTION")

    print(f"Prediction      : {prediction.upper()}")
    print(f"Confidence      : {confidence}%")

    # ---------------------------
    # Risk Analysis
    # ---------------------------

    risk_score, risk_level, reasons = calculate_risk(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        backlogs
    )

    print_section("RISK ANALYSIS")

    print(f"Risk Score      : {risk_score}/100")
    print(f"Risk Level      : {risk_level}")

    display_risk_factors(reasons)

    # ---------------------------
    # Weak Area Detection
    # ---------------------------

    strong_areas, weak_areas = analyze_performance(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        projects,
        skills_score
    )

    print_section("PERFORMANCE ANALYSIS")

    display_areas("Strong Areas", strong_areas)
    display_areas("Weak Areas", weak_areas)

    # ---------------------------
    # Suggestions
    # ---------------------------

    suggestions = generate_suggestions(
        attendance,
        internal_marks,
        study_hours,
        projects,
        backlogs,
        skills_score
    )

    print_section("IMPROVEMENT PLAN")

    display_suggestions(suggestions)

    # ---------------------------
    # Career Guidance
    # ---------------------------

    careers = recommend_careers(
        cgpa,
        projects,
        skills_score,
        extracurricular_score
    )

    print_section("CAREER GUIDANCE")

    display_careers(careers)

    # ---------------------------
    # Study Planner
    # ---------------------------

    study_plan = generate_study_plan(
        attendance,
        internal_marks,
        study_hours,
        backlogs,
        skills_score
    )

    print_section("PERSONALIZED STUDY PLAN")

    display_study_plan(study_plan)

    # ---------------------------
    # Academic Health Score
    # ---------------------------

    health_report = calculate_health_score(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        projects,
        backlogs,
        skills_score
    )

    print_section("ACADEMIC HEALTH SCORE")

    display_health_score(health_report)

    # ---------------------------
    # Explainable AI
    # ---------------------------

    feature_importance = get_feature_importance()

    print_section("EXPLAINABLE AI")

    display_feature_importance(feature_importance)

    # ---------------------------
    # Academic Advisor
    # ---------------------------

    advisor = academic_advisor(
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        backlogs
    )

    print_section("ACADEMIC ADVISOR")

    for advice in advisor:
        print(f"• {advice}")

    # ---------------------------
    # Database
    # ---------------------------

    try:
        add_student(
            student_name,
            student_email
        )
    except:
        pass

    save_prediction(
        student_email,
        prediction,
        confidence,
        risk_score,
        risk_level
    )

    # ---------------------------
    # PDF Report
    # ---------------------------

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

    print_section("REPORT GENERATED")

    print(f"Saved At : {report_path}")

    print("\nProject Execution Completed Successfully!")


if __name__ == "__main__":
    main()