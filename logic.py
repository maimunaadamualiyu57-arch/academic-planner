# logic.py

# Expanded student roster for Primary 4A
STUDENTS = [
    "Adamu Aliyu",
    "Fatima Bello",
    "Usman Sani",
    "Zainab Musa",
    "Aisha Garba",
    "Ibrahim Danladi"
]

def get_student_list():
    return STUDENTS

def save_test_scores(student_name, subject, test_score, exam_score):
    """Handles saving test and exam scores for a student."""
    if not student_name:
        return "Error: Please select a student."
    
    # You can expand this to save to a database or file later
    return f"Successfully saved! {subject} scores for {student_name}: Test = {test_score}, Exam = {exam_score}"

def save_attendance_record(student_name, attendance_date, status):
    """Handles recording daily attendance."""
    if not student_name:
        return "Error: Please select a student."
        
    return f"Attendance recorded: {student_name} was marked '{status}' on {attendance_date}."