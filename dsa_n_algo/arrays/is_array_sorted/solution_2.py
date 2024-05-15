# l = [1,2,4,7,7,5]
l = [1,2,3,4,5,6]

# bubble sort algo single loop
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True
        
result = is_sorted(l)        
print(result)