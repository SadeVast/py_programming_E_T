num = list(input("Введите числа:"))
b = int(input("Введите границу:"))
out = 0
for i in range(1, b + 1):
    if i not in num:
        #TODO
        out += i
print(out)

