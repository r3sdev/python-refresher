# Sets are a very useful collection type, allowing for blazing fast membership checks, in addition to providing a slew of handy methods for comparing collections.

# Among these methods are union, intersection, and difference. They work like this:

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}

# Combine set_1 and set_2
print(set_1.union(set_2))  # {1, 2, 3, 4, 5, 6, 7}

# Find common elements in set_1 and set_2
print(set_1.intersection(set_2))  # {3, 4, 5}

# Find elements in set_1 which are not in set_2
print(set_1.difference(set_2))  # {1, 2}

# These methods are great, but some of them have quite long names, and they take up a lot of space. Instead of using this method syntax, we can use special set operators like so:

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}

# Combine set_1 and set_2
print(set_1 | set_2)  # {1, 2, 3, 4, 5, 6, 7}

# Find common elements in set_1 and set_2
print(set_1 & set_2)  # {3, 4, 5}

# Find elements in set_1 which are not in set_2
print(set_1 - set_2)  # {1, 2}

# We can also chain the operations together, for example to find the union of three sets:

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}
set_3 = {5, 6, 7, 8, 9}

# Combine set_1 and set_2 and set_3
print(set_1 | set_2 | set_3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# One thing to note is that when using these set operators, rather than the method syntax, both operands must be sets. When using the method syntax, the argument can be any iterable type.