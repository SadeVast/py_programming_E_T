# Add a list with numbers.
a = [2, 5, 7, 6]
b = [5, 1, 4, 7]
c = []

for i in a:
    for j in b:
        if i == j:
            c.append(i)
            break
print(c)

if a == b:
    print("Lists are equal.")
elif len(a) == len(b):
    print("Equal list size.")
else:
    print("Lists are not equal.")
# TODO
