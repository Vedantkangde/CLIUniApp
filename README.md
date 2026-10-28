# CLIUniApp & GUIUniApp

University enrolment system written in Python 3 (no third-party libraries).

## Requirements
- Python 3.9 or newer
- `tkinter` 8.6+ for the GUI (bundled with the python.org installer; for Homebrew Python run
  `brew install python-tk@3.14`). On recent macOS, avoid Apple's `/usr/bin/python3` for the GUI:
  its old Tk 8.5 may show no window at all.

## Running
```bash
python3 main.py        # CLIUniApp (Admin + Student command-line system)
python3 gui_main.py    # GUIUniApp (student login + enrolment GUI)
```
Both apps share the same `students.data` file in the project root. It is created automatically
if it does not exist. Register students in the CLI first, then log in to the GUI with them.

## Project structure
```
main.py                     CLI entry point
gui_main.py                 GUI entry point
models/
  student.py                Student (6-digit id, name, email, password, subjects)
  subject.py                Subject (3-digit id, random mark 25-100, grade)
  database.py               Reads/writes Student objects to students.data (pickle)
controllers/
  university_controller.py  University System menu (A/S/X)
  student_controller.py     Student System menu (l/r/x) - login & register
  subject_controller.py     Student Course Menu (c/e/r/s/x)
  admin_controller.py       Admin System menu (c/g/p/r/s/x)
utils/
  validator.py              Email & password regex constants
  colors.py                 ANSI colours for the CLI output
gui/
  login_window.py           Login window (main window)
  enrolment_window.py       Enrolment window
  subject_window.py         Subject window (enrolled subjects, marks, grades)
  exception_window.py       Exception window (format errors, >4 subjects, etc.)
```

## Rules
- Email: `firstname.lastname@university.com`
- Password: starts with an upper-case letter, at least 5 more letters, then 3+ digits (e.g. `Helloworld123`)
- Grades: HD >= 85, D >= 75, C >= 65, P >= 50, Z < 50
- A student passes when their average mark is >= 50
- Maximum of 4 subjects per student

## Contributions
| Member | Area | Files | Contribution |
|--------|------|-------|--------------|
| Gautam Chamakochi (26059687) | Login & Registration | `main.py`, `controllers/university_controller.py`, `controllers/student_controller.py`, `utils/validator.py`, `utils/colors.py`, `gui_main.py`, `gui/login_window.py` | University System menu (A/S/X navigation); Student System login and register with email/password regex validation and duplicate-student checks; coloured output matching the sample I/O; GUIUniApp entry point and login window (main window, reads registered students from `students.data`). |
| Jose Joe (26508489) | Subject Enrolment | `models/student.py`, `models/subject.py`, `controllers/subject_controller.py`, `gui/enrolment_window.py` | `Student` and `Subject` models (random unique IDs, random marks 25-100, grade calculation, average mark and pass/fail); Student Course Menu for enrol (max 4), remove by ID, show and change password; GUIUniApp enrolment window (enrol in up to 4 subjects, saved to file). |
| Vedant Kangde (ID) | Admin & Data | `models/database.py`, `controllers/admin_controller.py`, `gui/subject_window.py`, `gui/exception_window.py` | `Database` class that creates `students.data` if missing and reads, writes, updates, removes and clears `Student` objects; Admin System to show, group by grade, partition PASS/FAIL, remove by ID and clear the database; GUIUniApp subject window (marks, grades and average) and exception window (empty fields, format errors, wrong credentials, 4-subject limit). |
