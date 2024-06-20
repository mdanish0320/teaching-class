"""
Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.

Pre-requisite: Longest subarray with given sum

Example 1:
Input Format: N = 4, array[] = [3, 1, 2, 4], k = 6
Result: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

"""

arr = [3, 1, 2, 4]
result = 6


occurane = 0
counter = 0
for i in range(len(arr)):
    total = 0
    for j in range(i, len(arr)):
        total += arr[j]
        if total == result:
            occurane += 1
print(occurane)