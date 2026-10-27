"""ANSI colour helpers used to match the colours in the sample I/O."""
import os

# Enables ANSI escape codes in the Windows terminal (no effect elsewhere)
if os.name == "nt":
    os.system("")

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"


def red(text):
    return f"{RED}{text}{RESET}"


def green(text):
    return f"{GREEN}{text}{RESET}"


def yellow(text):
    return f"{YELLOW}{text}{RESET}"


def cyan(text):
    return f"{CYAN}{text}{RESET}"
