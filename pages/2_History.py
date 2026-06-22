import streamlit as st
import pandas as pd

from database.database import get_prediction_history

st.set_page_config(
    page_title="Prediction History",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Prediction History")

st.markdown("---")

email = st.text_input(
    "Enter Student Email"
)

if st.button(
    "🔍 View History",
    use_container_width=True
):

    records = get_prediction_history(email)

    if records:

        df = pd.DataFrame(
            records,
            columns=[
                "ID",
                "Student Email",
                "Prediction",
                "Confidence",
                "Risk Score",
                "Risk Level",
                "Created At"
            ]
        )

        # ======================
        # METRICS
        # ======================

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total Predictions",
                len(df)
            )

        with col2:
            st.metric(
                "Average Confidence",
                f"{round(df['Confidence'].mean(), 2)}%"
            )

        st.markdown("---")

        # ======================
        # HISTORY TABLE
        # ======================

        st.subheader(
            "Prediction Records"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        # ======================
        # PDF DOWNLOAD
        # ======================

        st.markdown("---")

        try:

            pdf_path = "reports/priyanka_Report.pdf"

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="📄 Download Report",
                    data=pdf_file,
                    file_name="Student_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

        except FileNotFoundError:

            st.warning(
                "No PDF report available."
            )

    else:

        st.warning(
            "No prediction history found for this email."
        )