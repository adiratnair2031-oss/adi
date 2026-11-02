"""Student marks and grade calculator.

This module calculates the average of three marks for one student, assigns a
letter grade using fixed thresholds, and prints the student's name, average,
and grade. The marks are assigned directly in the script; the program does not
read any input from the user.

Grade thresholds (applied to the average):
    A: 90 or above
    B: 75 or above and below 90
    C: 50 or above and below 75
    F: below 50
"""


def calculate_average(a: int, b: int, c: int) -> float:
    """Calculate the arithmetic mean of three marks.

    Args:
        a: The first mark.
        b: The second mark.
        c: The third mark.

    Returns:
        The arithmetic mean of the three marks, as a float.
    """
    return (a + b + c) / 3


def calculate_grade(average: float) -> str:
    """Determine the grade for an average mark using fixed thresholds.

    The average is compared with the thresholds in order: "A" for 90 or above,
    "B" for 75 or above (and below 90), "C" for 50 or above (and below 75),
    and "F" for anything below 50. The function does not check whether the
    average is a valid mark.

    Args:
        average: The average mark to be graded.

    Returns:
        The grade: "A", "B", "C", or "F".
    """
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def display_result(name: str, average: float, grade: str) -> None:
    """Print a student's name, average, and grade.

    The average is rounded to two decimal places for display only.

    Args:
        name: The student's name.
        average: The student's average mark.
        grade: The grade assigned to the student.

    Returns:
        None. The function only prints the student's name, average, and grade.
    """
    print("Student:", name)
    print("Average:", round(average, 2))
    print("Grade:", grade)


student_name = "Anu"
mark1 = 85
mark2 = 78
mark3 = 92

average = calculate_average(mark1, mark2, mark3)
grade = calculate_grade(average)

display_result(student_name, average, grade)
