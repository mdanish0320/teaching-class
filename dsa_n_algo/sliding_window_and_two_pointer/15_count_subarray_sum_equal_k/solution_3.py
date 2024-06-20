"""
Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.

Pre-requisite: Longest subarray with given sum

Example 1:
Input Format: N = 4, array[] = [3, 1, 2, 4], k = 6
Result: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

video: https://www.youtube.com/watch?v=xvNwoz-ufXA&t=1161s
"""

# input
# arr = [3, 1, 2, 4]
arr = [1, 2, 3, -3, 1, 1, 1, 4, 2 , -3]
k = 3

# solution
res = 0
cur_sum = 0
pref_sum = { 0 : 1}

for i in arr:
    mapp = {0: 1}
    res = 0
    summ = 0
    target = 3

    for i in arr:
        summ += i
        diff = summ - target
        
        res += mapp.get(diff, 0)
        mapp[summ] = 1 + mapp.get(summ, 0)

print(res)

