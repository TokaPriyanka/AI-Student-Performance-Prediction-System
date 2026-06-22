import pandas as pd
import random

data = []

for i in range(1, 1001):

    cgpa = round(random.uniform(5.0, 10.0), 1)
    attendance = random.randint(40, 100)
    internal_marks = random.randint(35, 100)
    study_hours = random.randint(1, 8)
    projects = random.randint(0, 8)
    assignments_completed = random.randint(0, 20)
    extracurricular_score = random.randint(0, 10)
    sleep_hours = random.randint(4, 9)
    backlogs = random.randint(0, 5)
    skills_score = random.randint(1, 10)

    score = (
        cgpa * 12 +
        attendance * 0.30 +
        internal_marks * 0.40 +
        study_hours * 3 +
        projects * 4 +
        assignments_completed * 1 +
        extracurricular_score * 1.5 +
        skills_score * 3 -
        backlogs * 12
    )

    # Sleep impact
    if sleep_hours < 5:
        score -= 10
    elif sleep_hours > 8:
        score -= 3

    # Performance Classification
    if score >= 180:
        performance = "good"
    elif score >= 120:
        performance = "average"
    else:
        performance = "poor"

    data.append([
        i,
        cgpa,
        attendance,
        internal_marks,
        study_hours,
        projects,
        assignments_completed,
        extracurricular_score,
        sleep_hours,
        backlogs,
        skills_score,
        performance
    ])

df = pd.DataFrame(
    data,
    columns=[
        "student_id",
        "cgpa",
        "attendance",
        "internal_marks",
        "study_hours",
        "projects",
        "assignments_completed",
        "extracurricular_score",
        "sleep_hours",
        "backlogs",
        "skills_score",
        "performance"
    ]
)

df.to_csv(
    "data/StudentsPerformance.csv",
    index=False
)

print("1000 student records generated successfully!")