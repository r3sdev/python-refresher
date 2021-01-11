def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")
    
named(name="Bob", age=25)
print_nicely(name="Bob", age=25)

details = {"name": "Ramsy", "age": 40}
print_nicely(**details)

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)