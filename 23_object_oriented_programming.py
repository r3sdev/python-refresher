student = {"name": "Ramsy", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))


# OOP
class Student:
    # init method (function inside class is called a method)
    def __init__(self, name, grades):
        self.name = "Bob"
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (89, 90, 93, 88, 90))

print(student.name)
print(student.grades)
print(student.average_grade())

