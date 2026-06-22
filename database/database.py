# database/database.py

import sqlite3

DATABASE_PATH = "database/student.db"


def create_connection():
    return sqlite3.connect(DATABASE_PATH)


# -----------------------------
# CREATE TABLES
# -----------------------------
def create_tables():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_email TEXT,
        prediction TEXT,
        confidence REAL,
        risk_score INTEGER,
        risk_level TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# ADD STUDENT
# -----------------------------
def add_student(name, email):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students(name, email)
    VALUES (?, ?)
    """, (name, email))

    conn.commit()
    conn.close()


# -----------------------------
# SAVE PREDICTION
# -----------------------------
def save_prediction(
    email,
    prediction,
    confidence,
    risk_score,
    risk_level
):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions(
        student_email,
        prediction,
        confidence,
        risk_score,
        risk_level
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        email,
        prediction,
        confidence,
        risk_score,
        risk_level
    ))

    conn.commit()
    conn.close()


# -----------------------------
# GET HISTORY
# -----------------------------
def get_prediction_history(email):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM predictions
    WHERE student_email = ?
    ORDER BY created_at DESC
    """, (email,))

    records = cursor.fetchall()

    conn.close()

    return records


# -----------------------------
# GET ALL STUDENTS
# -----------------------------
def get_all_students():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM students
    """)

    students = cursor.fetchall()

    conn.close()

    return students


if __name__ == "__main__":
    create_tables()
    print("Database Ready!")