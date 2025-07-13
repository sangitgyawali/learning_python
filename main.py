# Class variables in Python

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name 
        self.age = age
        Student.num_students += 1

student1 = Student("Alex", 30)
student2 = Student("Milan", 35)
student3 = Student("Jay", 55)
student4 = Student("Frank", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students ")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
