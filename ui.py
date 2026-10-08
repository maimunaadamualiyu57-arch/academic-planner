# ui.py
import gradio as gr
from logic import get_student_list, save_test_scores, save_attendance_record

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📚 Academic Curriculum & Portal Tracker")
    
    with gr.Row():
        class_name = gr.Textbox(value="Primary 4A", label="Class Name", interactive=False)
        teacher_name = gr.Textbox(value="Maimuna Aliyu", label="Class Teacher Name")
    
    status_box = gr.Textbox(label="System Status", interactive=False)
    
    with gr.Tabs():
        # --- TAB 1: STUDENT RESULTS & TEST SCORES ---
        with gr.TabItem("Test Scores & Results"):
            gr.Markdown("### Upload or Update Student Test Scores")
            with gr.Row():
                student_dropdown = gr.Dropdown(
                    choices=get_student_list(), 
                    label="Select Student", 
                    interactive=True
                )
                subject_dropdown = gr.Dropdown(
                    choices=["English Studies", "Mathematics", "Basic Science", "Civic Education", "Social Studies"], 
                    label="Subject", 
                    interactive=True
                )
            
            with gr.Row():
                test_input = gr.Number(label="Continuous Assessment / Test Score (Max 30)")
                exam_input = gr.Number(label="Examination Score (Max 70)")
            
            submit_score_btn = gr.Button("Save Test Scores", variant="primary")
            score_output = gr.Textbox(label="Result Status")
            
            submit_score_btn.click(
                fn=save_test_scores,
                inputs=[student_dropdown, subject_dropdown, test_input, exam_input],
                outputs=[score_output]
            )

        # --- TAB 2: ATTENDANCE TRACKER ---
        with gr.TabItem("Attendance Tracker"):
            gr.Markdown("### Daily Class Attendance")
            with gr.Row():
                att_student_dropdown = gr.Dropdown(
                    choices=get_student_list(), 
                    label="Select Student", 
                    interactive=True
                )
                att_date = gr.Textbox(value="2026-10-06", label="Date (YYYY-MM-DD)")
            
            att_status = gr.Radio(
                choices=["Present", "Absent", "Late"], 
                label="Attendance Status", 
                value="Present"
            )
            
            submit_att_btn = gr.Button("Record Attendance", variant="primary")
            att_output = gr.Textbox(label="Attendance Status")
            
            submit_att_btn.click(
                fn=save_attendance_record,
                inputs=[att_student_dropdown, att_date, att_status],
                outputs=[att_output]
            )

        # --- TAB 3: PARENT-TEACHER CHAT ---
        with gr.TabItem("Parent-Teacher Chat & Notifications"):
            gr.Markdown("### Send Broadcast or Message to Parents")
            message_box = gr.Textbox(label="Type Notification Message")
            send_btn = gr.Button("Send Notification")
            chat_output = gr.Textbox(label="Delivery Status")
            
            send_btn.click(
                fn=lambda msg: f"Notification sent successfully: '{msg}'",
                inputs=[message_box],
                outputs=[chat_output]
            )
    demo.launch(share=True)