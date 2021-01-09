# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")

# if user_movie in movies_watched:
#     print("You have watched this before")
# else:
#     print("You haven't watched this before")

# number = 7

# while True:
#     user_input = input("Would you like to play? (Y/n) ")

#     if user_input == "n":
#         break

#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly")
#         break
#     elif abs(number - user_number) == 1: # number - user_number in (1, -1)
#         print("You were off by one")
#     else:
#         print("It's the wrong number")
    
    
friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(friend)

for n in range(4):
    print(n)

grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades) # length, 5

print(total / amount)



