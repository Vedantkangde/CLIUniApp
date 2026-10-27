import tkinter as tk
from tkinter import ttk

from gui.exception_window import ExceptionWindow
from gui.subject_window import SubjectWindow
from models.student import EnrolmentError, Student


class EnrolmentWindow(tk.Toplevel):
    def __init__(self, login_window, database, student):
        super().__init__(login_window)
        self.login_window = login_window
        self.database = database
        self.student = student
        self.subject_window = None

        self.title("GUIUniApp - Enrolment")
        self.geometry("380x260")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.logout)

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text=f"Welcome, {student.name}", font=("Helvetica", 15, "bold")).pack(anchor="w")
        ttk.Label(frame, text=f"Student ID: {student.id}").pack(anchor="w", pady=(2, 12))

        self.count_label = ttk.Label(frame)
        self.count_label.pack(anchor="w")
        self.status_label = ttk.Label(frame, foreground="#2e7d32")
        self.status_label.pack(anchor="w", pady=(4, 16))

        buttons = ttk.Frame(frame)
        buttons.pack(fill="x")
        ttk.Button(buttons, text="Enrol in Subject", command=self.enrol).pack(side="left")
        ttk.Button(buttons, text="View Subjects", command=self.show_subjects).pack(side="left", padx=8)
        ttk.Button(buttons, text="Logout", command=self.logout).pack(side="right")

        self.update_count()

    def update_count(self):
        self.count_label.config(
            text=f"You are enrolled in {len(self.student.subjects)} out of {Student.MAX_SUBJECTS} subjects"
        )

    def enrol(self):
        try:
            subject = self.student.enrol_subject()
        except EnrolmentError as error:
            ExceptionWindow(self, "Enrolment Error", str(error))
            return
        self.database.update_student(self.student)
        self.status_label.config(text=f"Enrolled in Subject-{subject.id} (mark {subject.mark}, grade {subject.grade})")
        self.update_count()
        if self.subject_window is not None and self.subject_window.winfo_exists():
            self.subject_window.refresh()

    def show_subjects(self):
        if self.subject_window is not None and self.subject_window.winfo_exists():
            self.subject_window.refresh()
            self.subject_window.lift()
        else:
            self.subject_window = SubjectWindow(self, self.student)

    def logout(self):
        self.destroy()
        self.login_window.show()
