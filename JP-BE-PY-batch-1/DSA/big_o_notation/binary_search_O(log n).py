"""
An algorithm with O(log n) complexity is typically associated with algorithms that 
divide the problem into smaller subproblems and solve each subproblem independently. 
A classic example is a binary search algorithm. Here's a simple implementation in Python:
"""


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 # mid = 5
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Found the target, return its index
        elif mid_value < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found in the array

# Example usage
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 5
result = binary_search(my_array, target_value)

if result != -1:
    print(f'Target {target_value} found at index {result}')
else:
    print(f'Target {target_value} not found in the array')
