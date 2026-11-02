def calculate_average(a, b, c):
    return (a + b + c) / 3

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

def display_result(name, average, grade):
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
