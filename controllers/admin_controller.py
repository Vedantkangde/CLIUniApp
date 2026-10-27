from utils.colors import cyan, red, yellow

INDENT = "\t"
GRADE_ORDER = ["HD", "D", "C", "P", "Z"]


class AdminController:
    def __init__(self, database):
        self.database = database

    def run(self):
        while True:
            choice = input(cyan(f"{INDENT}Admin System (c/g/p/r/s/x): ")).strip().lower()
            if choice == "c":
                self.clear_database()
            elif choice == "g":
                self.group_students()
            elif choice == "p":
                self.partition_students()
            elif choice == "r":
                self.remove_student()
            elif choice == "s":
                self.show_students()
            elif choice == "x":
                break
            else:
                print(red(f"{INDENT}Invalid option, please choose c, g, p, r, s or x"))

    def show_students(self):
        print(yellow(f"{INDENT}Student List"))
        students = self.database.read_students()
        if not students:
            print(f"{INDENT}\t< Nothing to Display >")
            return students
        for student in students:
            print(f"{INDENT}{student}")
        return students

    def group_students(self):
        print(yellow(f"{INDENT}Grade Grouping"))
        students = self.database.read_students()
        if not students:
            print(f"{INDENT}\t< Nothing to Display >")
            return
        groups = {}
        for student in students:
            groups.setdefault(student.grade(), []).append(student)
        for grade in GRADE_ORDER:
            if grade in groups:
                members = ", ".join(s.summary() for s in groups[grade])
                print(f"{INDENT}{grade:<2} --> [{members}]")

    def partition_students(self):
        print(yellow(f"{INDENT}PASS/FAIL Partition"))
        students = self.database.read_students()
        failed = ", ".join(s.summary() for s in students if not s.is_pass())
        passed = ", ".join(s.summary() for s in students if s.is_pass())
        print(f"{INDENT}FAIL --> [{failed}]")
        print(f"{INDENT}PASS --> [{passed}]")

    def remove_student(self):
        if not self.show_students():
            return
        student_id = input(f"{INDENT}Remove by ID: ").strip()
        if student_id.isdigit():
            student_id = student_id.zfill(6)
        if self.database.remove_student(student_id):
            print(yellow(f"{INDENT}Removing Student {student_id} Account"))
        else:
            print(red(f"{INDENT}Student {student_id} does not exist"))

    def clear_database(self):
        print(yellow(f"{INDENT}Clearing students database"))
        answer = input(red(f"{INDENT}Are you sure you want to clear the database (Y)ES/(N)O: ")).strip().upper()
        if answer == "Y":
            self.database.clear()
            print(yellow(f"{INDENT}Students data cleared"))
