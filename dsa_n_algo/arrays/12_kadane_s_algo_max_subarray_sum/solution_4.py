"""
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum.

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
total = 0

# overcome the nested loop iteration after each complete outer loop
for i in range(len(lst)):
    total += lst[i]
    if total > max_sum:
        max_sum = total
    
    if total < 0:
        total = 0
    
    
print(max_sum)
