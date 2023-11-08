from random import randint
# We create a list of random numbers.
n = 10
a = []
for i in range(n):
    a.append(randint(1, 99))
print(a)
# Sort the even index in ascending order.
a[::2] = sorted(a[::2])
# Sort the odd index in descending order.
a[1::2] = sorted(a[1::2], reverse=True)
print(a)
