import tkinter as tk
from tkinter import ttk


class ExceptionWindow(tk.Toplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)
        self.transient(parent)

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="⚠  " + title, font=("Helvetica", 14, "bold"), foreground="#c0392b").pack(anchor="w")
        ttk.Label(frame, text=message, wraplength=320, justify="left").pack(anchor="w", pady=(8, 16))
        ttk.Button(frame, text="OK", command=self.destroy).pack(anchor="e")

        self.bind("<Return>", lambda _event: self.destroy())
        self.bind("<Escape>", lambda _event: self.destroy())
        self.grab_set()
        self.focus_set()
