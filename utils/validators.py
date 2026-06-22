# utils/validators.py

import re


def validate_cgpa(cgpa):

    if 0 <= cgpa <= 10:
        return True

    return False


def validate_attendance(attendance):

    if 0 <= attendance <= 100:
        return True

    return False


def validate_internal_marks(marks):

    if 0 <= marks <= 100:
        return True

    return False


def validate_study_hours(hours):

    if 0 <= hours <= 24:
        return True

    return False


def validate_projects(projects):

    if projects >= 0:
        return True

    return False


def validate_backlogs(backlogs):

    if backlogs >= 0:
        return True

    return False


def validate_skills_score(score):

    if 0 <= score <= 10:
        return True

    return False


def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return bool(
        re.match(pattern, email)
    )


def validate_student_data(
    cgpa,
    attendance,
    internal_marks,
    study_hours,
    projects,
    backlogs,
    skills_score
):

    return all([
        validate_cgpa(cgpa),
        validate_attendance(attendance),
        validate_internal_marks(internal_marks),
        validate_study_hours(study_hours),
        validate_projects(projects),
        validate_backlogs(backlogs),
        validate_skills_score(skills_score)
    ])