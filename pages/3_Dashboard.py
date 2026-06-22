import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Academic Analytics Dashboard")

st.markdown("---")

# ======================
# LOAD DATABASE
# ======================

conn = sqlite3.connect(
    "database/student.db"
)

df = pd.read_sql_query(
    "SELECT * FROM predictions",
    conn
)

conn.close()

# ======================
# CHECK DATA
# ======================

if len(df) > 0:

    # ======================
    # TOP METRICS
    # ======================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Predictions",
            len(df)
        )

    with col2:
        st.metric(
            "Average Confidence",
            f"{round(df['confidence'].mean(), 2)}%"
        )

    with col3:
        st.metric(
            "Average Risk Score",
            round(df['risk_score'].mean(), 2)
        )

    with col4:

        most_common = (
            df["prediction"]
            .value_counts()
            .idxmax()
        )

        st.metric(
            "Most Common Prediction",
            most_common.upper()
        )

    st.markdown("---")

    # ======================
    # PIE CHARTS
    # ======================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "🎯 Prediction Distribution"
        )

        prediction_counts = (
            df["prediction"]
            .value_counts()
        )

        fig1, ax1 = plt.subplots()

        ax1.pie(
            prediction_counts,
            labels=prediction_counts.index,
            autopct="%1.1f%%"
        )

        st.pyplot(fig1)

    with col2:

        st.subheader(
            "⚠ Risk Level Distribution"
        )

        risk_counts = (
            df["risk_level"]
            .value_counts()
        )

        fig2, ax2 = plt.subplots()

        ax2.pie(
            risk_counts,
            labels=risk_counts.index,
            autopct="%1.1f%%"
        )

        st.pyplot(fig2)

    st.markdown("---")

    # ======================
    # LINE CHARTS
    # ======================

    col3, col4 = st.columns(2)

    with col3:

        st.subheader(
            "📈 Confidence Trend"
        )

        st.line_chart(
            df["confidence"]
        )

    with col4:

        st.subheader(
            "📉 Risk Score Trend"
        )

        st.line_chart(
            df["risk_score"]
        )

    st.markdown("---")

    # ======================
    # AI INSIGHTS
    # ======================

    st.subheader(
        "🧠 AI Insights"
    )

    avg_confidence = round(
        df["confidence"].mean(),
        2
    )

    avg_risk = round(
        df["risk_score"].mean(),
        2
    )

    st.success(
        f"Average confidence across predictions is {avg_confidence}%."
    )

    if avg_risk < 20:

        st.success(
            "Students generally have LOW academic risk."
        )

    elif avg_risk < 50:

        st.warning(
            "Students show MODERATE academic risk."
        )

    else:

        st.error(
            "Students show HIGH academic risk."
        )

    st.markdown("---")

    # ======================
    # DATASET
    # ======================

    st.subheader(
        "📋 Prediction Records"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.warning(
        "No prediction data available."
    )