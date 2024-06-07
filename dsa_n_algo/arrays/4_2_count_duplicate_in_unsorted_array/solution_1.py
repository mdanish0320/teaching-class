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
def count_duplicate_elements(arr):
    dictt = {}
    for j in range(len(arr)):
        if dictt.get( arr[j] ) is None:
            dictt[arr[j]] = 1
        else:
            dictt[arr[j]] += 1
    
    dupliates = 0
    for k, v in dictt.items():
        if v > 1:
            dupliates += v
    
    return dupliates

if __name__ == "__main__":
    arr = [1, 2, 3, 1, 1, 4]
    unique_count = count_duplicate_elements(arr)
    print(unique_count)