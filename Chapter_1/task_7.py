# Asking the user to enter a number
n = int(input("Please input positive num:"))
f = 1
if n > 0:
    # Adding a loop to factorial
    while (n):
        f *= n
        n -= 1
    print(f)
else:
    # Checking for a positive number
    print("Please input positive num")
