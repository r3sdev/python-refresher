from typing import List, Optional

class BadStudent:
    # Never assign a mutable object as a default parameter
    def __init__(self, name: str, grades: List[int] = []): # This is BAD!
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)

class GoodStudent:
    # Never assign a mutable object as a default parameter
    def __init__(self, name: str, grades: List[int] = None): # This is GOOD!
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

bob = BadStudent("Bob")
rolf = BadStudent("Rolf")

bob.take_exam(90)

print(bob.grades)
print(rolf.grades)

elza = GoodStudent("Elza")
pino = GoodStudent("Pino")

elza.take_exam(90)

print(elza.grades)
print(pino.grades)