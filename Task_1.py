student_marks = {
    "Aarav": 85,
    "Yuvraj": 92,
    "Priya": 78,
    "Sneha": 88,
    "Rohan": 74
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print(f"student not found '{student_name}'.")