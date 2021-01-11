class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")
    
    # often used as factories
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")

test = ClassTest()

test.instance_method()
# ClassTest.instance_method(test)

ClassTest.class_method()
ClassTest.static_method()

# Factory example
class Book:
    TYPES = ("harcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)

print(book)

hardcover = Book.hardcover("Harry Potter II", 1400)

print(hardcover)

paperback = Book.paperback("Python 101", 600)

print(paperback)

