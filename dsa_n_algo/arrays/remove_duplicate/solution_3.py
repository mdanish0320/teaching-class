from typing import List

# selection sort algo
def removeDuplicates(arr):
    i = 0
    for j in range(i + 1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
            
    # Slice the list to contain only the unique elements
    del arr[i+1:]

if __name__ == "__main__":
    arr = [1, 1, 1, 2, 3, 4]
    removeDuplicates(arr)
    print(arr)