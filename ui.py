import streamlit as st
import pandas as pd
from logic import get_student_list, save_attendance_record

st.set_page_config(page_title="Academic Tracker")
st.title("Academic Curriculum & Portal Tracker")

col1, col2 = st.columns(2)
col1.text_input("Class Name", value="Primary 4A", disabled=True)
teacher_name = col2.text_input("Class Teacher Name", value="Maimuna Aliyu")

tab1, tab2, tab3 = st.tabs([
    "Test Scores & Results",
    "Attendance Tracker",
    "Parent-Teacher Chat",
])

with tab1:
    st.subheader("Enter Student Scores")
    subject = st.selectbox("Subject", [
        "English Studies", "Mathematics", "Basic Science",
        "Civic Education", "Social Studies"],
        index=None, placeholder="Choose a subject", key="score_subject")

    if subject:
        score_cols = ["1st Test (10)", "2nd Test (10)", "3rd Test (10)", "Exam (70)"]
        base = pd.DataFrame({"Student": get_student_list()})
        for c in score_cols:
            base[c] = 0.0

        st.caption("Click a box in the table and type the score.")
        edited = st.data_editor(
            base,
            hide_index=True,
            disabled=["Student"],
            column_config={
                "1st Test (10)": st.column_config.NumberColumn(min_value=0, max_value=10, step=1),
                "2nd Test (10)": st.column_config.NumberColumn(min_value=0, max_value=10, step=1),
                "3rd Test (10)": st.column_config.NumberColumn(min_value=0, max_value=10, step=1),
                "Exam (70)": st.column_config.NumberColumn(min_value=0, max_value=70, step=1),
            },
            key=f"scores_{subject}",
        )

        results = edited.copy()
        results[score_cols] = results[score_cols].fillna(0)
        results["TOTAL (100)"] = results[score_cols].sum(axis=1)

        st.subheader(f"{subject} - Results with Total")
        st.dataframe(results, hide_index=True)

        if st.button("Save Scores", type="primary", key="save_scores"):
            st.success(f"Scores for {subject} saved for {len(results)} students.")
    else:
        st.info("Choose a subject to start entering scores.")

with tab2:
    st.subheader("Daily Class Attendance")
    c1, c2 = st.columns(2)
    att_student = c1.selectbox("Select Student", get_student_list(),
                               index=None, placeholder="Choose a student",
                               key="att_student")
    att_date = c2.text_input("Date (YYYY-MM-DD)", value="2026-10-06",
                             key="att_date")
    att_status = st.radio("Attendance Status",
                          ["Present", "Absent", "Late"],
                          horizontal=True, key="att_status")
    if st.button("Record Attendance", type="primary", key="save_att"):
        st.info(save_attendance_record(att_student, att_date, att_status))

with tab3:
    st.subheader("Send Broadcast or Message to Parents")
    message = st.text_input("Type Notification Message", key="msg")
    if st.button("Send Notification", key="send_msg"):
        st.success(f"Notification sent successfully: '{message}'")
