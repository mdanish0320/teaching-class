def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
        for j in range(0, n-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", my_list)

bubble_sort(my_list)

print("Sorted List:", my_list)
