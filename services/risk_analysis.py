# services/risk_analysis.py

def calculate_risk(
    cgpa,
    attendance,
    internal_marks,
    study_hours,
    backlogs
):

    risk_score = 0
    reasons = []

    # Attendance Analysis
    if attendance < 75:
        risk_score += 20
        reasons.append("Low Attendance")

    elif attendance < 85:
        risk_score += 10
        reasons.append("Attendance Below Recommended Level")

    # Internal Marks Analysis
    if internal_marks < 50:
        risk_score += 20
        reasons.append("Low Internal Marks")

    elif internal_marks < 70:
        risk_score += 10
        reasons.append("Average Internal Marks")

    # Study Hours Analysis
    if study_hours < 2:
        risk_score += 15
        reasons.append("Insufficient Study Hours")

    elif study_hours < 4:
        risk_score += 8
        reasons.append("Study Hours Can Be Improved")

    # Backlog Analysis
    if backlogs > 0:
        risk_score += backlogs * 12
        reasons.append(f"{backlogs} Backlog(s) Present")

    # CGPA Analysis
    if cgpa < 7:
        risk_score += 15
        reasons.append("Low CGPA")

    elif cgpa < 8:
        risk_score += 5
        reasons.append("CGPA Can Be Improved")

    # Limit Risk Score
    risk_score = min(risk_score, 100)

    # Risk Category
    if risk_score >= 60:
        risk_level = "HIGH"

    elif risk_score >= 30:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return risk_score, risk_level, reasons