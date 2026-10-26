import random


class Subject:
    """A subject a student is enrolled in, with a random mark and its grade."""

    MIN_MARK = 25
    MAX_MARK = 100

    def __init__(self, existing_ids=()):
        self.id = Subject.generate_id(existing_ids)
        self.mark = random.randint(Subject.MIN_MARK, Subject.MAX_MARK)
        self.grade = Subject.calculate_grade(self.mark)

    @staticmethod
    def generate_id(existing_ids=()):
        """Returns a unique 3-digit id between 001 and 999."""
        while True:
            new_id = f"{random.randint(1, 999):03d}"
            if new_id not in existing_ids:
                return new_id

    @staticmethod
    def calculate_grade(mark):
        if mark >= 85:
            return "HD"
        if mark >= 75:
            return "D"
        if mark >= 65:
            return "C"
        if mark >= 50:
            return "P"
        return "Z"

    def __str__(self):
        return f"[ Subject::{self.id} -- mark = {self.mark} -- grade = {self.grade:>3} ]"
