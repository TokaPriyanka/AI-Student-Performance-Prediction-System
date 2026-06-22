# services/suggestions.py

def generate_suggestions(
    attendance,
    internal_marks,
    study_hours,
    projects,
    backlogs,
    skills_score
):

    suggestions = []

    if attendance < 85:
        suggestions.append(
            f"Increase attendance from {attendance}% to at least 85%"
        )

    if internal_marks < 75:
        suggestions.append(
            "Improve internal marks above 75"
        )

    if study_hours < 4:
        suggestions.append(
            "Study at least 4 hours daily"
        )

    if projects < 3:
        suggestions.append(
            "Complete more academic or personal projects"
        )

    if backlogs > 0:
        suggestions.append(
            f"Clear {backlogs} backlog(s) as early as possible"
        )

    if skills_score < 7:
        suggestions.append(
            "Improve technical skills through certifications and practice"
        )

    if not suggestions:
        suggestions.append(
            "Excellent performance. Maintain consistency."
        )

    return suggestions