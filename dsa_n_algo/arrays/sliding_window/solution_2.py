def smallest_subarray_with_sum(arr, S):
    min_length = float('inf')
    window_sum = 0
    window_start = 0
    smallest_subarray = []

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add the next element to the window

        # Shrink the window as small as possible until the 'window_sum' is less than 'S'
        while window_sum >= S:
            if window_end - window_start + 1 < min_length:
                min_length = window_end - window_start + 1
                smallest_subarray = arr[window_start:window_end + 1]
            window_sum -= arr[window_start]
            window_start += 1

    return smallest_subarray

# Example usage:
input_arr = [2, 1, 5, 2, 8]
S = 7
print(smallest_subarray_with_sum(input_arr, S))  # Output: [8]
