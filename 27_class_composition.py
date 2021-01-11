# Composition is a counter part to Inheritance to
# build out classes that use other classes.
# This is used more than Inheritance
# 
# Composition comes in handy when like in this case
# a BookShelf has many Books

class BooksShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book("Python 101")

shelf = BooksShelf(book, book2)

print(shelf)
print(shelf.books)
