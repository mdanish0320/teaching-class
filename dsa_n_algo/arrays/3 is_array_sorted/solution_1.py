"""
Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. 
If the array is sorted then return True, Else return False.

Note: Two consecutive equal values are considered to be sorted.

Example 1:
Input:
 N = 5, array[] = {1,2,3,4,5}
Output
: True.
Explanation:
 The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.
 
"""

# l = [1,2,4,7,7,5]
# l = [1,2,3,4,5,6]
l = [5,4,3,2,1]

# bubble sort algorithm
for i in range(len(l)):
    is_sorted = True
    for j in range(len(l) - 1):
        if l[j] > l[j+1]:
            is_sorted = False
    if is_sorted == True:
        break
print(is_sorted)
    