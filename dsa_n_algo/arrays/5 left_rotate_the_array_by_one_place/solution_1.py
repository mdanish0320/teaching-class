"Problem Statement: Given an array of N integers, left rotate the array by one place."
"""
Example 1:
Input:
 N = 5, array[] = {1,2,3,4,5}
Output:
 2,3,4,5,1
"""

lst = [1, 2, 3, 4, 5]
rotated_list = []

for i in range(len(lst) -1):
    rotated_list.append(lst[i+1])

rotated_list.append(lst[0])
print(rotated_list)