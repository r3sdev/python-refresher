friend_ages = {"Cees": 40, "Kevin": 33, "Ferdinand": 40}

friend_ages["New"] = 1

print(friend_ages["Cees"])
print(friend_ages)

friends = [
    {"name": "Cees", "age": 40},
    {"name": "Kevin", "age": 33},
    {"name": "Ferdinand", "age": 40}
]

print(friends[0]["name"])


student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# better way
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))