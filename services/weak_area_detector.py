# services/weak_area_detector.py

def analyze_performance(
    cgpa,
    attendance,
    internal_marks,
    study_hours,
    projects,
    skills_score
):

    strong_areas = []
    weak_areas = []

    # CGPA
    if cgpa >= 8:
        strong_areas.append("CGPA")
    else:
        weak_areas.append("CGPA")

    # Attendance
    if attendance >= 85:
        strong_areas.append("Attendance")
    else:
        weak_areas.append("Attendance")

    # Internal Marks
    if internal_marks >= 75:
        strong_areas.append("Internal Marks")
    else:
        weak_areas.append("Internal Marks")

    # Study Hours
    if study_hours >= 4:
        strong_areas.append("Study Habits")
    else:
        weak_areas.append("Study Habits")

    # Projects
    if projects >= 3:
        strong_areas.append("Projects")
    else:
        weak_areas.append("Projects")

    # Skills
    if skills_score >= 7:
        strong_areas.append("Technical Skills")
    else:
        weak_areas.append("Technical Skills")

    return strong_areas, weak_areas