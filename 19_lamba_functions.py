# normal
def add(x, y):
    return x + y


result = lambda x, y: x + y

print(result, (lambda x, y: x + y)(5, 7))

def double(x):
    return x * 2

sequence = [1,3,5,9]

doubled = [double(x) for x in sequence] # list compehension is preferred over map

doubled_map = map(double, sequence)

doubled_lambda = [(lambda x: x * 2)(x) for x in sequence]

doubled_map_lambda = map(lambda x: x * 2, sequence)

print(doubled)
print(doubled_map)
print(doubled_lambda)
print(doubled_map_lambda)
print(list(doubled_map_lambda))

