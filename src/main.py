import tkinter as tk
from tkinter import filedialog
import os
from pathlib import Path


def get_num_courses() -> int:
    num_courses = None
    while num_courses is None:
        user_input = input("Number of courses: ")
        if user_input.isdigit():
            num_courses = int(user_input)
        else:
            print("Invalid input. Please enter an integer.")
    return num_courses


def get_course_info(num_courses: int) -> dict:
    course_info = {}

    for course in range(num_courses):
        print("\nCourse {}".format(course + 1))
        print("=========")
        course_code = input("Course Code: ")
        course_name = input("Course Name: ")
        course_info[course_code] = course_name

    return course_info


def get_directory_destination() -> Path:
    root = tk.Tk()
    root.withdraw()

    destination_directory = None

    while not destination_directory:
        destination_directory = filedialog.askdirectory(
            title="Select Destination Directory"
        )

        if not destination_directory:
            print("You need to pick dude.")

    return Path(destination_directory)


def create_directories(course_info: dict, course_root: Path) -> None:
    sub_directories = [
        "Midterm",
        "Final",
        "Slides",
        "Notes",
        "Readings",
        "Problems",
        "Misc",
    ]

    for course in course_info.keys():
        full_course = "{} {}".format(course, course_info[course])
        for directory in sub_directories:
            os.makedirs(course_root / full_course / directory, exist_ok=True)

    print("DONE!")


def main() -> None:
    num_courses = get_num_courses()
    course_info = get_course_info(num_courses)
    destination = get_directory_destination()
    create_directories(course_info, destination)


if __name__ == "__main__":
    main()
