numbers = [1, 3, 5]
doubled = [n * 2 for n in numbers]

# for n in numbers:
    # doubled.append(n * 2)

friends = ["Rolf", "Sam", "Samantha", "Sarah", "Jen"]

starts_s = []
starts_s_list_comp = [friend for friend in friends if friend.startswith("S")]

# Note: List comprehension creates a new list

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)
print(starts_s_list_comp)

print("friends:", id(friends), "starts_s:", id(starts_s))