people_list = [
    {
        "id": 1,
        "name": "danish"
    },
    {
        "id": 2,
        "name": "fahad"
    },
    {
        "id": 3,
        "name": "shoaib"
    },
]

people_list_2 = [
    {
        "id": 3,
        "name": "shoaib"
    },
    {
        "id": 4,
        "name": "shahzad"
    },
    {
        "id": 5,
        "name": "abdullah"
    },
]


def find_common(arr_1, arr_2):
    new_list = []
    for elem_1 in arr_1:
        for elem_2 in arr_2:
            if elem_1['id'] == elem_2['id']:
                new_list.append(elem_1)
    return new_list


new_list = find_common(people_list, people_list_2)
print(new_list)





def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
my_array = [64, 25, 12, 22, 11]
bubble_sort(my_array)

print("Sorted array:", my_array)