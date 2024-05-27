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


l = [1,2,4,7,7,5]
l = list(set(l)) # this is the issue in sorting solution, the duplicate hightest number

# bubble sort
for i in range(2):
    for j in range(len(l) - 1):
        if l[j] > l[j+1]:
            l[j], l[j+1]= l[j+1], l[j]

print(l[-2]) 



