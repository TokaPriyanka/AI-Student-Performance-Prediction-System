import streamlit as st

st.set_page_config(
    page_title="AI Student Performance System",
    page_icon="🎓",
    layout="wide"
)

# ======================
# HEADER
# ======================

st.title(
    "🎓 AI-Powered Student Performance Prediction System"
)

st.markdown(
    """
    ### Predict • Analyze • Guide • Improve
    """
)

st.markdown("---")

# ======================
# PROJECT OVERVIEW
# ======================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📌 Project Overview")

    st.write(
        """
        This intelligent academic analytics platform uses
        Machine Learning to predict student performance,
        identify academic risks, recommend improvement
        strategies, and provide career guidance.

        The system helps students understand their
        academic strengths, weaknesses, and future
        opportunities using AI-powered insights.
        """
    )



st.markdown("---")

# ======================
# PROJECT METRICS
# ======================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "Model Accuracy",
        "88%"
    )

with m2:
    st.metric(
        "ML Algorithm",
        "Random Forest"
    )

with m3:
    st.metric(
        "Database",
        "SQLite"
    )

with m4:
    st.metric(
        "Framework",
        "Streamlit"
    )

st.markdown("---")

# ======================
# MODULES
# ======================

st.subheader(
    "📂 Available Modules"
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info(
        """
        🎯 Prediction

        Predict student performance using ML.
        """
    )

with c2:
    st.info(
        """
        📚 History

        View previous predictions and reports.
        """
    )

with c3:
    st.info(
        """
        📊 Dashboard

        Analyze performance analytics.
        """
    )

with c4:
    st.info(
        """
        ℹ About

        Project details and technologies.
        """
    )

st.markdown("---")

# ======================
# FOOTER
# ======================

st.success(
    "👩‍💻 Developed By: Toka Priyanka"
)

st.caption(
    "AI-Powered Student Performance Prediction System"
)