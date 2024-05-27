"""
Exercise 1: Maximum Sum Subarray of Size K
Problem: Given an array of positive integers and a number k, find the maximum sum of any contiguous subarray of size k.

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
"""

# brute force
lst = [2, 1, 5, 1, 3, 2]
k = 3

max_sum = 0
for i in range(len(lst) - k ):
    total = sum(lst[i: i + k])
    if total > max_sum:
        max_sum = total
print(max_sum)


# optimal: calculate the sum only once
max_sum = 0
total = sum(lst[0:k])
max_total = total
for i in range(len(lst) - k):
    total -= lst[i]
    total += lst[i + k]
    max_total = max(max_total, total)
print(max_total)



