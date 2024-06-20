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

arr = [0,0,0,0,0]
goal = 0

cnt = 0
left = 0
right = 0
summ = 0

while left <= right:
    # print(left, right, summ)
    if summ < goal:
        right += 1
        if right == len(arr):
            break
        summ += arr[right]
        
    elif summ == goal:
        cnt += 1
        print(left, right, arr[left:right+1])
        
        
        summ -= arr[left]
        left += 1
        
    
    elif summ > goal:
        summ -= arr[left]
        left += 1

print(cnt)
