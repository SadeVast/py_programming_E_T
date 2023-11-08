from random import randint
# Row and Column Size
x, y = 3, 3
# Add list
matrix = []
matrix.append([i for i in range(y + 1)])
# Create matrix
for i in range(x + 1):
    matrix.append([i + 1, *[randint(0, 30) for j in range(y)]])

for i in range(x + 1):
    for j in range(y + 1):
        print(f'{matrix[i][j]:4d}', end='')
    print('')

# We ask which row and column to delete.
a, b = int(input("Удалить строку: ")), int(input("Удалить столбец: "))
# Delete using pop
matrix.pop(a)
for i in range(x):
    matrix[i].pop(b)

for i in range(x):
    for j in range(y):
        print(f'{matrix[i][j]:4d}', end='')
    print('')
