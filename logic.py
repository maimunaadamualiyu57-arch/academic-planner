 # logic.py

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

def calculate_total(first_test, second_test, third_test, exam):
    return first_test + second_test + third_test + exam

def save_all_scores(student_name, subject, first_test, second_test, third_test, exam):
    if not student_name:
        return "Error: Please select a student."
    if not subject:
        return "Error: Please select a subject."
    total = calculate_total(first_test, second_test, third_test, exam)
    return (f"Saved! {subject} for {student_name}: "
            f"1st Test = {first_test}, 2nd Test = {second_test}, "
            f"3rd Test = {third_test}, Exam = {exam}. TOTAL = {total}/100")

def save_test_scores(student_name, subject, test_score, exam_score):
    if not student_name:
        return "Error: Please select a student."
    return f"Saved! {subject} for {student_name}: Test = {test_score}, Exam = {exam_score}"

def save_attendance_record(student_name, attendance_date, status):
    if not student_name:
        return "Error: Please select a student."
    return f"Attendance recorded: {student_name} was marked '{status}' on {attendance_date}."
