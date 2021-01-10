# x, y are called parameters
def add(x, y):
    # pass # do nothing
    print(x +y)


# 5, 3 are called arguments
add(5, 3)

# positional arguments
def say_hello(name, surname):
    print(f"Hello {name} {surname}")

# named arguments
def say_hi(name = "Alan", surname = "Turing"):
    print(f"Hello {name} {surname}")

say_hello("Bob", "Marley")
say_hi("Donald","Trump")
say_hi()