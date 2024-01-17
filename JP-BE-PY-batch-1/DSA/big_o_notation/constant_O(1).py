"""
O(1) means that it takes a constant time to run an algorithm, regardless of the size of the input.
"""


def print_first_element(arr):
    # O(1) operation: accessing the first element of the array
    print(arr[0])

# Example usage
my_array = [1, 2, 3, 4, 5]
print_first_element(my_array)



###################################################################

def is_even(number):
    # O(1) operation: checking the parity of the number
    return number % 2 == 0

# Example usage
result = is_even(10)
print(result)  # Output: True
