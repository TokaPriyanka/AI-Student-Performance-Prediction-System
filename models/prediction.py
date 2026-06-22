# models/prediction.py

import pickle
import pandas as pd


# Load Trained Model
with open("models/trained_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load Encoder
with open("models/encoder.pkl", "rb") as encoder_file:
    encoder = pickle.load(encoder_file)


def predict_student(
    cgpa,
    attendance,
    internal_marks,
    study_hours,
    projects,
    assignments_completed,
    extracurricular_score,
    sleep_hours,
    backlogs,
    skills_score
):

    student_data = pd.DataFrame([{
        "cgpa": cgpa,
        "attendance": attendance,
        "internal_marks": internal_marks,
        "study_hours": study_hours,
        "projects": projects,
        "assignments_completed": assignments_completed,
        "extracurricular_score": extracurricular_score,
        "sleep_hours": sleep_hours,
        "backlogs": backlogs,
        "skills_score": skills_score
    }])

    prediction = model.predict(student_data)

    predicted_label = encoder.inverse_transform(
        prediction
    )[0]

    probabilities = model.predict_proba(
        student_data
    )

    confidence = round(
        max(probabilities[0]) * 100,
        2
    )

    return predicted_label, confidence


# Testing
if __name__ == "__main__":

    result, confidence = predict_student(
        cgpa=8.5,
        attendance=88,
        internal_marks=85,
        study_hours=5,
        projects=4,
        assignments_completed=15,
        extracurricular_score=7,
        sleep_hours=7,
        backlogs=0,
        skills_score=8
    )

    print("\nPrediction:", result)
    print("Confidence:", confidence, "%")