"""
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Example 1:
Input:
 arr = [-2,1,-3,4,-1,2,1,-5,4] 

Output:
 6 

Explanation:
 [4,-1,2,1] has the largest sum = 6. 
"""

lst = [-2,1,-3,4,-1,2,1,-5,4] 

max_sum = float("-inf")

# overcome the nested loop iteration after each complete outer loop
for i in range(len(lst)):
    for j in range(i, len(lst)):
        total = sum(lst[i: j])
        if total > max_sum:
            sub_array = lst[i: j]
            max_sum = total
    
print(max_sum, sub_array)
