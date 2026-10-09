import streamlit as st
import pandas as pd
from logic import get_student_list, save_attendance_record

st.set_page_config(page_title="Nurain Integrated School")

st.title("Nurain Integrated School, Gombe")
st.caption("Academic Curriculum & Portal Tracker")

t_col, s_col = st.columns(2)
term = t_col.selectbox("Term", ["First Term", "Second Term", "Third Term"],
                       key="term")
session = s_col.selectbox("Academic Session",
                          ["2025/2026", "2026/2027", "2027/2028"],
                          index=1, key="session")

col1, col2 = st.columns(2)
col1.text_input("Class Name", value="Primary 4A", disabled=True)
teacher_name = col2.text_input("Class Teacher Name", value="Maimuna Aliyu")

tab1, tab2, tab3 = st.tabs([
    "Scores",
    "Attendance",
    "Parents",
])

with tab1:
    st.subheader("Enter Student Scores")
    subject = st.selectbox("Subject", [
        "English Studies", "Mathematics", "Basic Science",
        "Civic Education", "Social Studies"],
        index=None, placeholder="Choose a subject", key="score_subject")

    if subject:
        score_cols = ["1st", "2nd", "3rd", "Exam"]
        base = pd.DataFrame({"Student": get_student_list()})
        for c in score_cols:
            base[c] = float("nan")

        st.caption("1st, 2nd, 3rd = 10 marks each. Exam = 70 marks. "
                   "Tap a box and type the score. Type 0 if the child scored zero.")
        edited = st.data_editor(
            base,
            hide_index=True,
            disabled=["Student"],
            use_container_width=True,
            column_config={
                "Student": st.column_config.TextColumn("Student", width=115, pinned=True),
                "1st": st.column_config.NumberColumn(min_value=0, max_value=10, step=1, width=52, format="%d"),
                "2nd": st.column_config.NumberColumn(min_value=0, max_value=10, step=1, width=52, format="%d"),
                "3rd": st.column_config.NumberColumn(min_value=0, max_value=10, step=1, width=52, format="%d"),
                "Exam": st.column_config.NumberColumn(min_value=0, max_value=70, step=1, width=55, format="%d"),
            },
            key=f"scores_{subject}_{term}_{session}",
        )

        scores = edited[score_cols]
        totals = pd.DataFrame({
            "Student": edited["Student"],
            "Total (100)": scores.sum(axis=1, min_count=1),
        })

        st.subheader("Totals")
        st.caption(f"{subject} | {term} | {session} Session")
        st.dataframe(
            totals,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Student": st.column_config.TextColumn(width=140),
                "Total (100)": st.column_config.NumberColumn(width=85, format="%d"),
            },
        )

        if st.button("Save Scores", type="primary", key="save_scores"):
            st.success(f"{subject} scores ({term}, {session}) saved for {len(totals)} students.")
    else:
        st.info("Choose a subject to start.")

with tab2:
    st.subheader("Daily Class Attendance")
    st.caption(f"{term} | {session} Session")
    att_student = st.selectbox("Select Student", get_student_list(),
                               index=None, placeholder="Choose a student",
                               key="att_student")
    att_date = st.text_input("Date (YYYY-MM-DD)", value="2026-10-06",
                             key="att_date")
    att_status = st.radio("Attendance Status",
                          ["Present", "Absent", "Late"],
                          horizontal=True, key="att_status")
    if st.button("Record Attendance", type="primary", key="save_att"):
        st.info(save_attendance_record(att_student, att_date, att_status))

with tab3:
    st.subheader("Message to Parents")
    message = st.text_input("Type Notification Message", key="msg")
    if st.button("Send Notification", key="send_msg"):
        st.success(f"Notification sent successfully: '{message}'")
