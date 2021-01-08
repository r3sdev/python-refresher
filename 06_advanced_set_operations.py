friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)

print(friends)
print(abroad)
print(local_friends)
print(abroad.difference(friends)) # set() = empty set

local_friends = {"Rolf"}
abroad_friends = {"Bob", "Anne"}
friends = local_friends.union(abroad_friends)

print(friends)


art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)

print(both)

