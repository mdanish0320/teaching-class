"""
Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.

Pre-requisite: Longest subarray with given sum

Example 1:
Input Format: N = 4, array[] = [3, 1, 2, 4], k = 6
Result: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

"""

# input
arr = [3, 1, 2, 4]
k = 6

# solution
res = 0
cur_sum = 0
pref_sum = { 0 : 1}

for i in arr:
    cur_sum += i
    diff = cur_sum - k
    print("curr", cur_sum, "diff", diff, pref_sum.get(diff, 0))
    res += pref_sum.get(diff, 0)
    pref_sum[cur_sum] = 1 + pref_sum.get(cur_sum, 0)

    # print(pref_sum)

# print(res)

"""
{0: 1, 3: 1}                        # first loop (3) = 3,           diff = -3
{0: 1, 3: 1, 4: 1}                  # second loop (3 + 1) = 4,      diff = -2
{0: 1, 3: 1, 4: 1, 6: 1}            # third (3 + 1 + 2) = 6         diff = 0
{0: 1, 3: 1, 4: 1, 6: 1, 10: 1}     # fourth (3 + 1 + 2 + 4) = 10   diff = 4
"""

