# Create a tuple entered by the user.
txt = tuple(input("Enter text:"))
# Distance between elements.
interval = int(input("Interval:"))

A = txt
B = (A[i] for i in range(0, len(txt), interval))

print(*A)
print(*B)
