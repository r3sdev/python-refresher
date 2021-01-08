# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")

# if user_movie in movies_watched:
#     print("You have watched this before")
# else:
#     print("You haven't watched this before")

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y": #user_input in ("y","Y")
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly")
    elif abs(number - user_number) == 1: # number - user_number in (1, -1)
        print("You were off by one")
    else:
        print("It's the wrong number")
