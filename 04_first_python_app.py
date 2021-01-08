user_age = int(input("Enter your age: "))
months = user_age * 12
hours = 365 * 24 * months
minutes = hours * 60
seconds = minutes * 60

print(f"Your age, {user_age} in years, is {months} months, {hours} hours, {minutes} minutes, {seconds} seconds")