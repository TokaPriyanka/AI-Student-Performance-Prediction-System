# utils/helper.py


def print_section(title):

    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def display_risk_factors(reasons):

    if not reasons:
        print("No major risk factors detected.")
        return

    for reason in reasons:
        print(f"• {reason}")


def display_areas(title, areas):

    print(f"\n{title}")

    if not areas:
        print("None")
        return

    for area in areas:
        print(f"• {area}")


def display_suggestions(suggestions):

    print()

    for i, suggestion in enumerate(
        suggestions,
        start=1
    ):
        print(f"{i}. {suggestion}")


def display_careers(careers):

    print()

    for index, (career, score) in enumerate(
        careers,
        start=1
    ):
        print(
            f"{index}. {career} "
            f"({score}% Match)"
        )


def display_study_plan(plan):

    for day, tasks in plan.items():

        print(f"\n{day.upper()}")

        if not tasks:
            print("Rest / Revision")

        else:
            for task in tasks:
                print(f"• {task}")


def display_health_score(report):

    print(
        f"Overall Score : "
        f"{report['overall_score']}/100"
    )

    print(
        f"Status        : "
        f"{report['status']}"
    )

    print(
        f"Attendance    : "
        f"{report['attendance_score']}"
    )

    print(
        f"Marks         : "
        f"{report['marks_score']}"
    )

    print(
        f"CGPA          : "
        f"{report['cgpa_score']}"
    )

    print(
        f"Study Habits  : "
        f"{report['study_score']}"
    )

    print(
        f"Projects      : "
        f"{report['project_score']}"
    )

    print(
        f"Skills        : "
        f"{report['skill_score']}"
    )

    print(
        f"Backlogs      : "
        f"{report['backlog_score']}"
    )


def display_feature_importance(features):

    for index, (feature, score) in enumerate(
        features,
        start=1
    ):
        print(
            f"{index}. "
            f"{feature} : "
            f"{score}%"
        )