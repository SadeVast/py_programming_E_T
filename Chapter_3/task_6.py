from random import randint
# We create a list of random numbers.
n = 10
a = []
for i in range(n):
    a.append(randint(1, 99))
print(a)
"""
We sequentially compare the values of neighboring elements,
and if the value of the element on the left is greater than the value of the element on the right,
the elements are swapped.
"""

for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j + 1], a[j]

print(a)
