# Adding a try function.
try:
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    # Checking which number is greater using the ternary operator.
    print("This number is greater:", a if a > b else b)
except:
    # The user entered a non-integer number.
    print("You must enter an integer!")
