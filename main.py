# Class variables in Python

class Student:

    class_year = 2025

    def __init__(self, name, age):
        self.name = name 
        self.age = age

student1 = Student("Alex", 30)
student2 = Student("Milan", 35)

print(student2.name)
print(student2.age)
print(Student.class_year)