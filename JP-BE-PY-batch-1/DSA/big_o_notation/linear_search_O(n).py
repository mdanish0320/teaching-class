my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 5

def find_val_place_in_arr(my_array, target_value):
    for i in range(len(my_array)):
        if my_array[i] == target_value:
            return i  # Found the target, return its index
    return -1  # Target not found in the list

place = find_val_place_in_arr(my_array, target_value)
print(place)

