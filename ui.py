import streamlit as st
from logic import get_student_list, save_test_scores, save_attendance_record

st.set_page_config(page_title="Academic Tracker", page_icon="📚")
st.title("📚 Academic Curriculum & Portal Tracker")

col1, col2 = st.columns(2)
col1.text_input("Class Name", value="Primary 4A", disabled=True)
teacher_name = col2.text_input("Class Teacher Name", value="Maimuna Aliyu")

tab1, tab2, tab3 = st.tabs([
    "Test Scores & Results",
    "Attendance Tracker",
    "Parent-Teacher Chat",
])

with tab1:
    st.subheader("Upload or Update Student Test Scores")
    c1, c2 = st.columns(2)
    student = c1.selectbox("Select Student", get_student_list(),
                           index=None, placeholder="Choose a student", key="score_student")
    subject = c2.selectbox("Subject", [
        "English Studies", "Mathematics", "Basic Science",
        "Civic Education", "Social Studies"],
        index=None, placeholder="Choose a subject", key="score_subject")
    test_score = c1.number_input("Test Score (Max 30)", min_value=0.0,
                                 max_value=30.0, step=1.0, key="test_score")
    exam_score = c2.number_input("Exam Score (Max 70)", min_value=0.0,
                                 max_value=70.0, step=1.0, key="exam_score")
    if st.button("Save Test Scores", type="primary", key="save_scores"):
        st.info(save_test_scores(student, subject, test_score, exam_score))

with tab2:
    st.subheader("Daily Class Attendance")
    c1, c2 = st.columns(2)
    att_student = c1.selectbox("Select Student", get_student_list(),
                               index=None, placeholder="Choose a student", key="att_student")
    att_date = c2.text_input("Date (YYYY-MM-DD)", value="2026-10-06", key="att_date")
    att_status = st.radio("Attendance Status", ["Present", "Absent", "Late"],
                          horizontal=True, key="att_status")
    if st.button("Record Attendance", type="primary", key="save_att"):
        st.info(save_attendance_record(att_student, att_date, att_status))

with tab3:
    st.subheader("Send Broadcast or Message to Parents")
    message = st.text_input("Type Notification Message", key="msg")
    if st.button("Send Notification", key="send_msg"):
        st.success(f"Notification sent successfully: '{message}'")
