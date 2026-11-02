# Student Grade Calculator

A beginner Python program that asks for a student's marks and prints the matching grade.

## Description

`student_grade_calculator.py` reads one mark from the keyboard, checks that it is between 0 and 100, and prints a grade using fixed thresholds. The grading is done by a single function, `calculate_grade(marks)`.

## Features

- Reads a mark as a decimal number (for example `85` or `72.5`).
- Accepts marks from 0 to 100 only; any other number gives a message asking for marks between 0 and 100.
- Returns one of six grades: A+, A, B, C, D or F.

## Grade Thresholds

| Marks | Grade |
|---|---|
| 90 and above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | F |

## Requirements

- Python 3
- No external libraries are needed.

## Installation

1. Download or clone the repository:
   ```
   git clone https://github.com/adiratnair2031-oss/adi.git
   ```
2. Open the folder in a terminal or in VS Code.

## Usage

Run the program and type a mark when asked:

```
python student_grade_calculator.py
```

## Example

```
Enter marks: 85
Grade: A
```

```
Enter marks: 101
Please enter marks between 0 and 100.
```

## Project Structure

```
adi/
├── student_grade_calculator.py
└── README_Student_Grade_Calculator.md
```

(The repository also contains other lab files; only the files for this program are shown.)

## Limitations

- Only one mark is handled each time the program runs.
- Typing something that is not a number (for example `abc`) stops the program with a `ValueError`, because the input is not checked before it is converted.

## Future Improvements

- Handle non-numeric input without crashing.
- Allow several students or subjects in one run.
- Add tests for the grade boundaries (90, 80, 70, 60 and 50).

## Author

Adira T Nair
