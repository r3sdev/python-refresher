class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Define string representation
    def __str__(self):
        return f"Person {self.name}, {self.age} years old"
    
    # Define developer representation, used in debugger etc.
    def __repr(self):
        return f"<Person('{self.name}', {self.age})>"

bob = Person("Bob", 35)

print(bob) # __str__
