# Membership operators in Python

grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

student = input("Enter the student's name: ")

if student in grades:
    print(f"{student} has a grade of {grades[student]}.")
else:
    print(f"{student} is not in the gradebook.")

