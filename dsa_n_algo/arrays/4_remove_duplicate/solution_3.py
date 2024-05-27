"""
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.

Example 1:
Input:
 arr[1,1,2,2,2,3,3]

Output:
 arr[1,2,3,_,_,_,_]

Explanation:
 Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.
"""

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