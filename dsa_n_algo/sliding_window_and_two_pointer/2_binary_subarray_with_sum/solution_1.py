"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
"""

arr = [1,0,1,0,1]
goal = 2

cnt = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if sum(arr[i:j+1]) == goal:
            cnt +=1
print(cnt)