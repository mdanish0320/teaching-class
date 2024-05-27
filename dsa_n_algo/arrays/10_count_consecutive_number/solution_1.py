"""
Count Maximum Consecutive One's in the array

Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

Example 1:

Input: prices = [1, 1, 0, 1, 1, 1]

Output: 3

Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

"""

nums = [1, 1, 0, 1, 1, 1, 0]

count = 0
max_count = 0

for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
    else:
        count = 0
    
    if count > 0 and count > max_count:
        max_count += 1

print(max_count)