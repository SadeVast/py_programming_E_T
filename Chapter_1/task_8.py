# Asking the user to enter a number
n = int(input("Enter the number:"))
fib1 = fib2 = 1
print(fib1, fib2, end=' ')
# Add a loop in which we assign the sum to the variables
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')



