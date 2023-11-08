# Asking the user to enter a number
number = input("Enter Number:")
# Create a tuple entered by the user.
res_tuple = tuple(int(i) for i in number)
# In reverse order
res_tuple_reverse = tuple(int(i) for i in number[::-1])

print(res_tuple)
print(res_tuple_reverse)
