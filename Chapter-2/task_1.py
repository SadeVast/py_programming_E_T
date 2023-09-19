# Ask the user to enter an integer.
number = int(input("Enter number:"))
i = 0
# Determine how many digits are in a number using a loop.
while number > 0:
    i += 1
    number = number // 10
print("Number of digits in a number:", i)
