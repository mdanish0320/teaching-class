"""
Problem Statement: Given an array, we have to find the largest element in the array.

Example 1:
Input:
 arr[] = {2,5,1,3,0};
Output:5
Explanation: 5 is the largest element in the array.
"""

arr = [2, 5, 1, 3, 0]

h = 0
for i in arr:
    if i > h:
        h = i
print(h)