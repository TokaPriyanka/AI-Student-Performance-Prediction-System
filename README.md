# 🎓 AI-Powered Student Performance Prediction, Risk Analysis & Career Guidance System

## 📌 Project Overview

The AI-Powered Student Performance Prediction System is an intelligent academic analytics platform designed to evaluate student performance, identify academic risks, recommend improvement strategies, and provide career guidance using Machine Learning techniques.

The system analyzes multiple academic and behavioral factors such as CGPA, attendance, internal marks, study habits, project involvement, assignments, extracurricular activities, technical skills, sleep patterns, and backlogs to predict overall student performance.

In addition to prediction, the platform provides personalized academic insights including risk assessment, weak area detection, study planning, career recommendations, academic health scoring, explainable AI insights, and downloadable performance reports.

---

## 🎯 Objectives

- Predict student academic performance using Machine Learning.
- Identify students at academic risk.
- Detect weak and strong academic areas.
- Generate personalized improvement suggestions.
- Recommend suitable career paths.
- Create customized study plans.
- Provide explainable AI insights.
- Generate professional PDF reports.
- Maintain student records using SQLite database.

---

## 🚀 Key Features

### 1. Student Performance Prediction
Predicts whether a student belongs to:

- Good Performance
- Average Performance
- Poor Performance

Machine Learning Model:
- Random Forest Classifier

---

### 2. Academic Risk Analysis

Calculates:

- Academic Risk Score (0-100)
- Risk Level

Categories:

- Low Risk
- Medium Risk
- High Risk

Factors Considered:

- Attendance
- Internal Marks
- Study Hours
- CGPA
- Backlogs

---

### 3. Weak Area Detection

Identifies:

#### Strong Areas
- CGPA
- Attendance
- Internal Marks
- Technical Skills
- Projects

#### Weak Areas
- Low Attendance
- Low Study Hours
- Poor Academic Scores
- Skill Gaps

---

### 4. Personalized Improvement Suggestions

Provides customized recommendations such as:

- Increase attendance
- Improve study consistency
- Complete additional projects
- Strengthen technical skills
- Clear academic backlogs

---

### 5. Career Guidance Engine

Recommends career paths based on academic profile and skills.

Example Careers:

- AI / ML Engineer
- Data Scientist
- Data Analyst
- Software Developer
- Project Manager

Each recommendation includes a career match score.

---

### 6. Personalized Study Planner

Generates weekly study plans tailored to student weaknesses and academic goals.

Includes:

- Revision Schedule
- Coding Practice
- Backlog Preparation
- Assignment Planning
- Skill Development Activities

---

### 7. Academic Health Score

Provides an overall academic wellness score based on:

- CGPA
- Attendance
- Internal Marks
- Projects
- Skills
- Study Habits
- Backlogs

Performance Categories:

- Excellent
- Good
- Average
- Needs Improvement

---

### 8. Explainable AI Module

Displays the contribution of each feature to the final prediction.

Example:

- CGPA → 22%
- Attendance → 18%
- Internal Marks → 17%
- Skills Score → 12%

This improves transparency and model interpretability.

---

### 9. PDF Report Generation

Generates downloadable performance reports containing:

- Student Details
- Prediction Results
- Risk Analysis
- Academic Health Score
- Career Recommendations
- Study Plan
- Improvement Suggestions

---

### 10. Database Management

SQLite Database Integration

Stores:

- Student Information
- Prediction History
- Performance Reports
- Academic Analytics

---

## 🧠 Machine Learning Workflow

```text
Student Data
      ↓
Data Validation
      ↓
Feature Processing
      ↓
Random Forest Model
      ↓
Performance Prediction
      ↓
Risk Analysis
      ↓
Weak Area Detection
      ↓
Suggestions Generation
      ↓
Career Guidance
      ↓
Study Plan Creation
      ↓
Academic Health Score
      ↓
PDF Report Generation
```

## 📊 Dataset Features

The model is trained using the following attributes:

- CGPA
- Attendance
- Internal Marks
- Study Hours
- Projects
- Assignments Completed
- Extracurricular Score
- Sleep Hours
- Backlogs
- Skills Score

Target Variable:

- Performance

Categories:

- Good
- Average
- Poor

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- Random Forest Classifier

### Data Processing
- Pandas
- NumPy

### Database
- SQLite

### Reporting
- ReportLab

### Frontend (Future Integration)
- Streamlit

### AI Features
- Explainable AI
- Academic Advisor

---

## 📁 Project Structure

```text
Student_Performance_AI/
│
├── data/
├── database/
├── models/
├── services/
├── utils/
├── reports/
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 📈 Model Performance

- Dataset Size: 1000+ Records
- Algorithm: Random Forest Classifier
- Accuracy Achieved: ~88%
- Evaluation Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1 Score

---

## 🔮 Future Enhancements

- Streamlit Interactive Dashboard
- Student Login & Registration
- Prediction History Tracking
- Real-Time Analytics Dashboard
- AI Chatbot Academic Advisor
- Email Notifications
- Cloud Deployment
- Multi-Student Performance Monitoring
- Faculty Dashboard

---

## 👩‍💻 Author

**Toka Priyanka**

B.Tech Computer Science Engineering  
GITAM School of Technology

---

## 📄 License

This project is developed for educational and research purposes.