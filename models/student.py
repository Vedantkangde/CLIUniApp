import random

from models.subject import Subject


class EnrolmentError(Exception):
    """Raised when a student tries to enrol in more than the allowed subjects."""


class Student:
    """A registered student and the subjects they are enrolled in."""

    MAX_SUBJECTS = 4
    PASS_MARK = 50

    def __init__(self, name, email, password, existing_ids=()):
        self.id = Student.generate_id(existing_ids)
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    @staticmethod
    def generate_id(existing_ids=()):
        """Returns a unique 6-digit id between 000001 and 999999."""
        while True:
            new_id = f"{random.randint(1, 999999):06d}"
            if new_id not in existing_ids:
                return new_id

    def is_full(self):
        return len(self.subjects) >= Student.MAX_SUBJECTS

    def enrol_subject(self):
        if self.is_full():
            raise EnrolmentError(f"Students are allowed to enrol in {Student.MAX_SUBJECTS} subjects only")
        subject = Subject([s.id for s in self.subjects])
        self.subjects.append(subject)
        return subject

    def remove_subject(self, subject_id):
        """Removes the subject with the given id. Returns True if it was found."""
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                return True
        return False

    def change_password(self, new_password):
        self.password = new_password

    def average_mark(self):
        if not self.subjects:
            return 0.0
        return sum(s.mark for s in self.subjects) / len(self.subjects)

    def grade(self):
        return Subject.calculate_grade(self.average_mark())

    def is_pass(self):
        return self.average_mark() >= Student.PASS_MARK

    def summary(self):
        """Format used by the admin grouping and partition output."""
        return f"{self.name} :: {self.id} --> GRADE: {self.grade():>2} - MARK: {self.average_mark():.2f}"

    def __str__(self):
        return f"{self.name} :: {self.id} --> Email: {self.email}"
