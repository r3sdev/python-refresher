# Mosts things in Python are mutable

# Lists are mutable
a = []
b = a

print("a", id(a))
print("b", id(b)) # a & b are references to the same object

c = []
d = []

c.append(35)

print("c", id(c))
print("d", id(d)) # c & are referencing two different objects

# Tuples are immutable
e = ()
f = ()

print("e1", id(e))
e = e + (15,)

print("e2", id(e))
print("f", id(f))

# Ints, floats, booleans and strings are immutable and optimisation gives them the same ID
g = 8597
h = 8597

print("g", id(g))
print("h", id(h))

