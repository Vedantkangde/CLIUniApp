import re

EMAIL_PATTERN = r"^[A-Za-z]+\.[A-Za-z]+@university\.com$"

PASSWORD_PATTERN = r"^[A-Z][A-Za-z]{5,}[0-9]{3,}$"


def is_valid_email(email):
    return re.match(EMAIL_PATTERN, email) is not None


def is_valid_password(password):
    return re.match(PASSWORD_PATTERN, password) is not None


def is_valid_credentials(email, password):
    return is_valid_email(email) and is_valid_password(password)
