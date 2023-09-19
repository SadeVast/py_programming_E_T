# Ask the user to enter an integer.
number = int(input("Enter number:"))
# Add a loop and raise to a power.
while number > 0:
    digit = number % 10
    print(str(digit), end="")
    number = number // 10
