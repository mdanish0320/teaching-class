"""
Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Example 1:
Input:
 [1,2,4,7,7,5]
Output:
 Second Smallest : 2
	Second Largest : 5
Explanation:
 The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2
"""

# explanation: https://www.youtube.com/watch?v=YetqNl-E5Zw
# efficient way

l = [1,2,4,7,7,5]
# l = [10, 10, 10]

h = float("-inf")
sh = float("-inf")
for i in range(len(l)):
    if l[i] > h:
        h = l[i]
    elif l[i] > sh and l[i] != h:
        sh = l[i]

print(h, sh)