import os
import pickle

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "students.data")


class Database:
    def __init__(self, path=DATA_FILE):
        self.path = path
        self.ensure_file()

    def ensure_file(self):
        if not os.path.exists(self.path):
            self.write_students([])

    def read_students(self):
        self.ensure_file()
        try:
            with open(self.path, "rb") as file:
                students = pickle.load(file)
                return students if isinstance(students, list) else []
        except (EOFError, pickle.UnpicklingError, AttributeError, ImportError):
            return []

    def write_students(self, students):
        with open(self.path, "wb") as file:
            pickle.dump(students, file)

    def find_by_email(self, email):
        for student in self.read_students():
            if student.email.lower() == email.lower():
                return student
        return None

    def find_by_id(self, student_id):
        for student in self.read_students():
            if student.id == student_id:
                return student
        return None

    def existing_ids(self):
        return [s.id for s in self.read_students()]

    def add_student(self, student):
        students = self.read_students()
        students.append(student)
        self.write_students(students)

    def update_student(self, updated):
        students = self.read_students()
        for index, student in enumerate(students):
            if student.id == updated.id:
                students[index] = updated
                break
        self.write_students(students)

    def remove_student(self, student_id):
        students = self.read_students()
        remaining = [s for s in students if s.id != student_id]
        if len(remaining) == len(students):
            return False
        self.write_students(remaining)
        return True

    def clear(self):
        self.write_students([])
