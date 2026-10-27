"""Regular expressions used to validate student credentials."""
import re

# firstname.lastname@university.com
EMAIL_PATTERN = r"^[A-Za-z]+\.[A-Za-z]+@university\.com$"

# Starts with an upper-case letter, has at least five more letters,
# and ends with three or more digits (e.g. Helloworld123)
PASSWORD_PATTERN = r"^[A-Z][A-Za-z]{5,}[0-9]{3,}$"


def is_valid_email(email):
    return re.match(EMAIL_PATTERN, email) is not None


def is_valid_password(password):
    return re.match(PASSWORD_PATTERN, password) is not None


def is_valid_credentials(email, password):
    return is_valid_email(email) and is_valid_password(password)
