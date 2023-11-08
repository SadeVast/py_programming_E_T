from random import randint
# We create a list of random numbers.
n = 10
a = []
for i in range(n):
    a.append(randint(1, 10))
print(a)

insert = 1
stop = len(a) + len(a) - 1

while insert != stop:
    a.insert(insert, a[insert - 1] + a[insert])
    insert += 2

print(a)
