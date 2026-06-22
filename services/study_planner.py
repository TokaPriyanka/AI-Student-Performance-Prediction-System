# services/study_planner.py

def generate_study_plan(
    attendance,
    internal_marks,
    study_hours,
    backlogs,
    skills_score
):

    plan = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    # Attendance Improvement
    if attendance < 85:
        plan["Monday"].append("Attend all classes")
        plan["Thursday"].append("Review missed topics")

    # Internal Marks Improvement
    if internal_marks < 75:
        plan["Tuesday"].append("2 hrs Subject Revision")
        plan["Friday"].append("Practice Previous Questions")

    # Study Hours Improvement
    if study_hours < 4:
        plan["Wednesday"].append("Increase study time by 1-2 hours")
        plan["Saturday"].append("Complete pending assignments")

    # Backlogs
    if backlogs > 0:
        plan["Monday"].append("Backlog Subject Practice")
        plan["Wednesday"].append("Backlog Topic Revision")
        plan["Sunday"].append("Mock Test for Backlog Subjects")

    # Skills Improvement
    if skills_score < 7:
        plan["Tuesday"].append("1 hr Coding Practice")
        plan["Friday"].append("Work on Mini Project")
        plan["Sunday"].append("Learn New Technology")

    # Good Student
    if (
        attendance >= 85 and
        internal_marks >= 75 and
        study_hours >= 4 and
        backlogs == 0 and
        skills_score >= 7
    ):
        plan["Monday"].append("Advanced Learning")
        plan["Wednesday"].append("Competitive Coding")
        plan["Friday"].append("Project Development")
        plan["Sunday"].append("Mock Interview Practice")

    return plan