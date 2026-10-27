from controllers.subject_controller import SubjectController
from models.student import Student
from utils.colors import cyan, green, red, yellow
from utils.validator import is_valid_credentials

INDENT = "\t"


class StudentController:
    """Student System menu: login and register."""

    def __init__(self, database):
        self.database = database

    def run(self):
        while True:
            choice = input(cyan(f"{INDENT}Student System (l/r/x): ")).strip().lower()
            if choice == "l":
                self.login()
            elif choice == "r":
                self.register()
            elif choice == "x":
                break
            else:
                print(red(f"{INDENT}Invalid option, please choose l, r or x"))

    def read_credentials(self):
        """Prompts until the email and password match the required formats."""
        while True:
            email = input(f"{INDENT}Email: ").strip()
            password = input(f"{INDENT}Password: ").strip()
            if is_valid_credentials(email, password):
                print(yellow(f"{INDENT}email and password formats acceptable"))
                return email, password
            print(red(f"{INDENT}Incorrect email or password format"))

    def login(self):
        print(green(f"{INDENT}Student Sign In"))
        email, password = self.read_credentials()
        student = self.database.find_by_email(email)
        if student is None or student.password != password:
            print(red(f"{INDENT}Student does not exist"))
            return
        SubjectController(self.database, student).run()

    def register(self):
        print(green(f"{INDENT}Student Sign Up"))
        email, password = self.read_credentials()
        existing = self.database.find_by_email(email)
        if existing is not None:
            print(red(f"{INDENT}Student {existing.name} already exists"))
            return

        name = input(f"{INDENT}Name: ").strip()
        while not name:
            print(red(f"{INDENT}Name cannot be empty"))
            name = input(f"{INDENT}Name: ").strip()

        print(yellow(f"{INDENT}Enrolling Student {name}"))
        student = Student(name, email, password, self.database.existing_ids())
        self.database.add_student(student)
