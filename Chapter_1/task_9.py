# Create a list of numbers
n_list = [2, 3, 10, 6, 8]


# Create a function
def sec_largest(n_list):
    # Sort the list in ascending order and display the second-largest value
    n_list.sort()
    print("The second largest element of the list is:", n_list[-2])


# Deriving a function
sec_largest(n_list)
