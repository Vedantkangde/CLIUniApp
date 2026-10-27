from controllers.admin_controller import AdminController
from controllers.student_controller import StudentController
from models.database import Database
from utils.colors import cyan, red, yellow


class UniversityController:
    """Top-level menu that navigates between the Admin and Student subsystems."""

    def __init__(self):
        self.database = Database()

    def run(self):
        while True:
            choice = input(cyan("University System: (A)dmin, (S)tudent, or X : ")).strip().upper()
            if choice == "A":
                AdminController(self.database).run()
            elif choice == "S":
                StudentController(self.database).run()
            elif choice == "X":
                print(yellow("Thank You"))
                break
            else:
                print(red("Invalid option, please choose A, S or X"))
