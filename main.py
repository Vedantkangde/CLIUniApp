from controllers.university_controller import UniversityController
from utils.colors import yellow


def main():
    try:
        UniversityController().run()
    except (KeyboardInterrupt, EOFError):
        print(yellow("\nThank You"))


if __name__ == "__main__":
    main()
