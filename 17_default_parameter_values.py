def add(x, y=1):
    print(x + y)

add(5)

# don't do this because changing the default value afterwards
# does not change the function

default_y = 3

def add_with_default(x, y=default_y):
    print(x + y)

add_with_default(1)

default_y = 4

add_with_default(1)
