# services/career_guidance.py

def recommend_careers(
    cgpa,
    projects,
    skills_score,
    extracurricular_score
):

    careers = []

    # AI / ML Engineer
    ai_score = (
        cgpa * 3 +
        projects * 5 +
        skills_score * 6
    )

    careers.append((
        "AI / Machine Learning Engineer",
        min(round(ai_score), 100)
    ))

    # Data Scientist
    ds_score = (
        cgpa * 4 +
        skills_score * 5 +
        projects * 4
    )

    careers.append((
        "Data Scientist",
        min(round(ds_score), 100)
    ))

    # Software Developer
    dev_score = (
        cgpa * 4 +
        projects * 6 +
        skills_score * 4
    )

    careers.append((
        "Software Developer",
        min(round(dev_score), 100)
    ))

    # Data Analyst
    analyst_score = (
        cgpa * 4 +
        skills_score * 4 +
        extracurricular_score * 2
    )

    careers.append((
        "Data Analyst",
        min(round(analyst_score), 100)
    ))

    # Project Manager
    pm_score = (
        extracurricular_score * 7 +
        cgpa * 3 +
        skills_score * 2
    )

    careers.append((
        "Project Manager",
        min(round(pm_score), 100)
    ))

    # Sort by Match Score
    careers.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return careers[:5]