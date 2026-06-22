import streamlit as st

st.set_page_config(
    page_title="AI Academic Advisor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Academic Advisor")

st.caption(
    "Ask questions about academics, skills, career planning and performance improvement."
)

st.markdown("---")

st.info("""
🤖 Welcome to AI Academic Advisor

You can ask questions related to:

📈 CGPA Improvement

📚 Attendance

📝 Internal Marks

📅 Study Planning

💻 Technical Skills

🚀 Career Guidance

⚠ Backlogs

🔮 Personalized AI recommendations coming soon.
""")

question = st.text_input(
    "Ask your question...",
    placeholder="Example: How can I improve my CGPA?"
)

if st.button(
    "🚀 Get Advice",
    use_container_width=True
):

    question = question.lower()

    if "cgpa" in question:

        st.success("""
📈 Tips to Improve CGPA

• Study consistently every day

• Focus on weak subjects

• Prepare well for internals

• Maintain attendance above 85%

• Revise before examinations
""")

    elif "attendance" in question:

        st.success("""
📚 Tips to Improve Attendance

• Attend classes regularly

• Avoid unnecessary leaves

• Track attendance weekly

• Participate in classroom activities
""")

    elif "internal" in question or "marks" in question:

        st.success("""
📝 Tips to Improve Internal Marks

• Submit assignments on time

• Perform well in quizzes

• Complete lab work regularly

• Prepare for internal exams
""")

    elif "skills" in question:

        st.success("""
💻 Skills Development Tips

• Practice coding daily

• Build real-world projects

• Learn Python and SQL

• Participate in hackathons

• Improve problem-solving skills
""")

    elif "career" in question:

        st.success("""
🚀 Career Guidance

• Build strong technical skills

• Complete internships

• Create a GitHub portfolio

• Learn AI/ML and Data Analytics

• Improve communication skills
""")

    elif "study" in question:

        st.success("""
📅 Recommended Study Plan

Monday → Coding Practice

Tuesday → Core Subjects

Wednesday → Projects

Thursday → Revision

Friday → Aptitude Practice

Weekend → Mock Tests
""")

    elif "backlog" in question:

        st.warning("""
⚠ Backlog Recovery Plan

• Prioritize backlog subjects

• Create a weekly revision schedule

• Solve previous papers

• Seek faculty guidance

• Focus on one backlog at a time
""")

    else:

        st.info("""
🤖 I can currently help with:

• CGPA Improvement

• Attendance

• Internal Marks

• Study Plans

• Skills Development

• Career Guidance

• Backlogs

Try asking:

• How can I improve my CGPA?

• Career guidance

• How to improve skills?

• Backlog recovery plan
""")

st.markdown("---")

st.subheader("🚀 Upcoming Features")

st.write("""
• Personalized AI Recommendations

• Prediction-Based Guidance

• Career Roadmap Generation

• Resume Suggestions

• Interview Preparation Assistance

• AI-Powered Academic Analytics
""")

st.success(
    "Future versions will provide personalized recommendations based on student prediction data."
)