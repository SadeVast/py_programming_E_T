# Todo comments
n = int(input("Please input positive num:"))
f = 1
if n > 0:
    while (n):
        f *= n
        n -= 1
    print(f)
else:
    print("Please input positive num")
