print("Welcome to the Number Collector Program! Please enter 3 numbers when prompted.") # Greets user and explains what the program does

#prompts user to enter 3 numbers and stores them. Each number has a try/except block to catch any numbers that are not a valid integer. If the user enters a non-integer, the program will use 0 as the number instead.
try:
    number1 = int(input("Please enter your 1st number:"))
except ValueError:
    print("I'm sorry, that isn't a valid number. I will use 0 as your number instead.")
    number1 = 0
try:
    number2 = int(input("Please enter your 2nd number:"))
except ValueError:
    print("I'm sorry, that isn't a valid number. I will use 0 as your number instead.")
    number2 = 0
try:
    number3 = int(input("Please enter your 3rd number:"))
except ValueError:
    print("I'm sorry, that isn't a valid number. I will use 0 as your number instead.")
    number3 = 0

#Calulates the sum and average of the given numbers.
sum = number1 + number2 + number3
average = sum / 3

#prints the information calculated from the user input.
print(f"Your numbers are: {number1}, {number2}, and {number3}.")
print(f"The sum of your numbers is: {sum}")
print(f"The average of your numbers is: {average:.2f}")
