"Problem Statement: Given an array of N integers, left rotate the array by one place."
"""
Example 1:
Input:
 N = 5, array[] = {1,2,3,4,5}
Output:
 2,3,4,5,1
"""

lst = [1, 2, 3, 4, 5]

first_element = lst[0]
for i in range(len(lst) - 1):
    lst[i] = lst[i + 1]
lst[-1] = first_element

print(lst)