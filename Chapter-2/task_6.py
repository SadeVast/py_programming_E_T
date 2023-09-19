# Ask users side of the triangle
a = int(input("Enter the first side of the triangle ="))
b = int(input("Enter the second side of the triangle ="))
c = int(input("Enter the last side ="))
# Create a condition where the sum of two sides is greater than the third.
if a + b > c and b + c > a and a + c > b:
    print("The triangle exists.")
# The sum of two sides is less than the third.
else:
    print("The triangle doesn't exist.")