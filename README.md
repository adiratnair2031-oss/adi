# Student Marks and Grade Calculator

## Project Description

This program calculates the average of three marks for one student, assigns a grade using fixed thresholds, and displays the student's name, average, and grade. It is written as three Python functions: `calculate_average()`, `calculate_grade()`, and `display_result()`.

## Features

- Calculates the arithmetic mean of three marks.
- Assigns grade A, B, C, or F from the average.
- Displays the student's name, average (rounded to two decimal places), and grade.
- A documented version, `student_marks_documented.py`, adds a module docstring, function docstrings, and type hints without changing the program's behaviour.

## Software Requirements

- Python 3
- Visual Studio Code (used to write and run the program)
- No external libraries are required.

## How to Run in VS Code

1. Open the project folder in VS Code (**File → Open Folder**).
2. Open `student_marks.py` (or `student_marks_documented.py`).
3. Run the file with the **Run Python File** button, or open **Terminal → New Terminal** and enter:

   ```
   python student_marks.py
   ```

   If your Windows system uses the Python launcher, use `py student_marks.py`.

The marks and the student's name are assigned inside the program (`student_name`, `mark1`, `mark2`, `mark3`). The program does not ask the user for input.

## Example Run

```
Student: Anu
Average: 85.0
Grade: B
```

## Grade Thresholds

| Average | Grade |
|---|---|
| 90 or higher | A |
| 75 or higher and below 90 | B |
| 50 or higher and below 75 | C |
| Below 50 | F |

## Project Structure

```
Module4_Code_Documentation/
├── student_marks.py
├── student_marks_documented.py
├── README.md
└── documentation_review.md
```

## Limitations

- Only one predefined test case (Anu: 85, 78, 92) is used.
- The program handles exactly three marks for one student.
- The marks are not checked, so values outside a valid range (for example, 150 or -20) are graded without an error.
- The grade thresholds may not match every grading system.
