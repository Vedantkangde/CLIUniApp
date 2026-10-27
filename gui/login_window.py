import tkinter as tk
from tkinter import ttk

from gui.enrolment_window import EnrolmentWindow
from gui.exception_window import ExceptionWindow
from models.database import Database
from utils.validator import is_valid_email, is_valid_password


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.database = Database()

        self.title("GUIUniApp - Student Login")
        self.geometry("360x240")
        self.resizable(False, False)

        frame = ttk.Frame(self, padding=24)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="Student Sign In", font=("Helvetica", 16, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 16)
        )
        ttk.Label(frame, text="Email:").grid(row=1, column=0, sticky="w", pady=4)
        self.email_entry = ttk.Entry(frame)
        self.email_entry.grid(row=1, column=1, sticky="ew", pady=4)
        ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky="w", pady=4)
        self.password_entry = ttk.Entry(frame, show="•")
        self.password_entry.grid(row=2, column=1, sticky="ew", pady=4)

        ttk.Button(frame, text="Login", command=self.login).grid(row=3, column=1, sticky="e", pady=(16, 0))

        self.bind("<Return>", lambda _event: self.login())
        self.email_entry.focus_set()

        self.lift()
        self.attributes("-topmost", True)
        self.after(300, lambda: self.attributes("-topmost", False))
        self.focus_force()

    def login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            ExceptionWindow(self, "Empty Fields", "Please enter both your email and password.")
            return
        if not is_valid_email(email):
            ExceptionWindow(self, "Format Error", "Incorrect email format.\nExample: firstname.lastname@university.com")
            return
        if not is_valid_password(password):
            ExceptionWindow(
                self,
                "Format Error",
                "Incorrect password format.\nIt must start with an upper-case letter, contain at least "
                "five more letters and end with three or more digits (e.g. Helloworld123).",
            )
            return

        student = self.database.find_by_email(email)
        if student is None or student.password != password:
            ExceptionWindow(self, "Login Failed", "Student does not exist or the credentials are incorrect.")
            return

        self.withdraw()
        EnrolmentWindow(self, self.database, student)

    def show(self):
        self.password_entry.delete(0, "end")
        self.deiconify()
        self.email_entry.focus_set()
