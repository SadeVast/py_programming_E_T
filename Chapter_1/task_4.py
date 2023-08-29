# Asking the user how many numbers are in the list
find = int(input("How many:"))
# Create a list containing a power of two
nums = [2 ** a for a in range(find)]
# Output variable
print(nums)
