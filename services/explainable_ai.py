# services/explainable_ai.py

import pickle


def get_feature_importance():

    with open("models/trained_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    feature_names = [
        "CGPA",
        "Attendance",
        "Internal Marks",
        "Study Hours",
        "Projects",
        "Assignments Completed",
        "Extracurricular Score",
        "Sleep Hours",
        "Backlogs",
        "Skills Score"
    ]

    importance_values = model.feature_importances_

    feature_importance = []

    for feature, importance in zip(
        feature_names,
        importance_values
    ):
        feature_importance.append(
            (
                feature,
                round(importance * 100, 2)
            )
        )

    feature_importance.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return feature_importance