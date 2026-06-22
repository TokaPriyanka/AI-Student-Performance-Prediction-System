# services/academic_health_score.py

def calculate_health_score(
    cgpa,
    attendance,
    internal_marks,
    study_hours,
    projects,
    backlogs,
    skills_score
):

    attendance_score = attendance

    marks_score = internal_marks

    cgpa_score = (cgpa / 10) * 100

    study_score = min((study_hours / 8) * 100, 100)

    project_score = min((projects / 8) * 100, 100)

    skill_score = min((skills_score / 10) * 100, 100)

    backlog_score = max(100 - (backlogs * 20), 0)

    overall_score = round(
        (
            attendance_score +
            marks_score +
            cgpa_score +
            study_score +
            project_score +
            skill_score +
            backlog_score
        ) / 7,
        2
    )

    if overall_score >= 85:
        status = "EXCELLENT"

    elif overall_score >= 70:
        status = "GOOD"

    elif overall_score >= 50:
        status = "AVERAGE"

    else:
        status = "NEEDS IMPROVEMENT"

    return {
        "overall_score": overall_score,
        "status": status,
        "attendance_score": round(attendance_score, 2),
        "marks_score": round(marks_score, 2),
        "cgpa_score": round(cgpa_score, 2),
        "study_score": round(study_score, 2),
        "project_score": round(project_score, 2),
        "skill_score": round(skill_score, 2),
        "backlog_score": round(backlog_score, 2)
    }