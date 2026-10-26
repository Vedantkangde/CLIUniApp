import tkinter as tk
from tkinter import ttk

from models.student import Student


class SubjectWindow(tk.Toplevel):
    """Lists the logged-in student's enrolled subjects with marks and grades."""

    def __init__(self, parent, student):
        super().__init__(parent)
        self.student = student
        self.title("GUIUniApp - Enrolled Subjects")
        self.geometry("420x300")

        frame = ttk.Frame(self, padding=16)
        frame.pack(fill="both", expand=True)

        self.heading = ttk.Label(frame, font=("Helvetica", 13, "bold"))
        self.heading.pack(anchor="w")

        columns = ("id", "mark", "grade")
        self.table = ttk.Treeview(frame, columns=columns, show="headings", height=Student.MAX_SUBJECTS)
        for column, label in zip(columns, ("Subject ID", "Mark", "Grade")):
            self.table.heading(column, text=label)
            self.table.column(column, anchor="center", width=110)
        self.table.pack(fill="x", pady=10)

        self.summary = ttk.Label(frame)
        self.summary.pack(anchor="w")

        ttk.Button(frame, text="Close", command=self.destroy).pack(anchor="e", pady=(10, 0))
        self.refresh()

    def refresh(self):
        self.heading.config(text=f"Showing {len(self.student.subjects)} subjects")
        self.table.delete(*self.table.get_children())
        for subject in self.student.subjects:
            self.table.insert("", "end", values=(f"Subject::{subject.id}", subject.mark, subject.grade))
        status = "PASS" if self.student.is_pass() else "FAIL"
        self.summary.config(
            text=f"Average mark: {self.student.average_mark():.2f}   Grade: {self.student.grade()}   ({status})"
        )
