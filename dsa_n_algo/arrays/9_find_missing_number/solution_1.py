"""
Find the missing number in an array
Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
                    Find the number(between 1 to N), that is not present in the given array.

Example 1:
Input Format:
 N = 5, array[] = {1,2,4,5}
Result:
 3
Explanation: 
In the given array, number 3 is missing. So, 3 is the answer.                    
"""

lst = [1, 2, 4, 5] # number starts from 1
lst = [10, 11, 13, 14] # number starts from anywhere
# lst = [10, 11, 14, 15] # multiple missing numbers

lst = sorted(lst) # ascending order

missing_number = 0
for i in range(len(lst)):
    if lst[i+1] - lst[i] > 1:
        missing_number = lst[i+1] - 1
        break 

print(missing_number)


