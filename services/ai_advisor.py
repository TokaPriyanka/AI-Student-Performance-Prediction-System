# services/ai_advisor.py

def academic_advisor(
    cgpa,
    attendance,
    internal_marks,
    study_hours,
    backlogs
):

    advice = []

    if cgpa < 8:
        advice.append(
            "Focus on improving semester performance to increase CGPA."
        )

    if attendance < 85:
        advice.append(
            "Improve attendance to at least 85%."
        )

    if internal_marks < 75:
        advice.append(
            "Spend more time on subject revision and mock tests."
        )

    if study_hours < 4:
        advice.append(
            "Study at least 4 hours daily."
        )

    if backlogs > 0:
        advice.append(
            "Prioritize clearing backlog subjects."
        )

    if not advice:
        advice.append(
            "Excellent academic performance. Continue your current strategy."
        )

    return advice