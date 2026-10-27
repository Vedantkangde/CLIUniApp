from models.student import EnrolmentError, Student
from utils.colors import cyan, red, yellow
from utils.validator import is_valid_password

INDENT = "\t\t"


class SubjectController:
    def __init__(self, database, student):
        self.database = database
        self.student = student

    def run(self):
        while True:
            choice = input(cyan(f"{INDENT}Student Course Menu (c/e/r/s/x): ")).strip().lower()
            if choice == "c":
                self.change_password()
            elif choice == "e":
                self.enrol()
            elif choice == "r":
                self.remove()
            elif choice == "s":
                self.show()
            elif choice == "x":
                break
            else:
                print(red(f"{INDENT}Invalid option, please choose c, e, r, s or x"))

    def save(self):
        self.database.update_student(self.student)

    def change_password(self):
        print(yellow(f"{INDENT}Updating Password"))
        new_password = input(f"{INDENT}New Password: ").strip()
        while not is_valid_password(new_password):
            print(red(f"{INDENT}Incorrect password format"))
            new_password = input(f"{INDENT}New Password: ").strip()

        confirm = input(f"{INDENT}Confirm Password: ").strip()
        while confirm != new_password:
            print(red(f"{INDENT}Password does not match - try again"))
            confirm = input(f"{INDENT}Confirm Password: ").strip()

        self.student.change_password(new_password)
        self.save()

    def enrol(self):
        try:
            subject = self.student.enrol_subject()
        except EnrolmentError as error:
            print(red(f"{INDENT}{error}"))
            return
        self.save()
        print(yellow(f"{INDENT}Enrolling in Subject-{subject.id}"))
        print(yellow(f"{INDENT}You are now enrolled in {len(self.student.subjects)} out of {Student.MAX_SUBJECTS} subjects"))

    def remove(self):
        subject_id = input(f"{INDENT}Remove Subject by ID: ").strip()
        if subject_id.isdigit():
            subject_id = subject_id.zfill(3)
        if not self.student.remove_subject(subject_id):
            print(red(f"{INDENT}Subject {subject_id} does not exist"))
            return
        self.save()
        print(yellow(f"{INDENT}Dropping Subject-{subject_id}"))
        print(yellow(f"{INDENT}You are now enrolled in {len(self.student.subjects)} out of {Student.MAX_SUBJECTS} subjects"))

    def show(self):
        print(yellow(f"{INDENT}Showing {len(self.student.subjects)} subjects"))
        for subject in self.student.subjects:
            print(f"{INDENT}{subject}")
