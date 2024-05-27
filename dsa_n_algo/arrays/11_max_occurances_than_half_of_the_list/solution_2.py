"""
Find the Majority Element that occurs more than N/2 times

Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. 
                    You may consider that such an element always exists in the array.


Example 1:
Input Format
: N = 3, nums[] = {3,2,3}
Result
: 3
Explanation
: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 
"""

lst = [2,2,1,1,1,2,2,2, 3]
dictt = {}
max_occurance = 0

for i in range(len(lst)):
    if dictt.get( lst[i] ) is None:
        dictt[lst[i]] = 1
    else:
        dictt[lst[i]] += 1

for k, v in dictt.items():
    if v > len(lst)//2:
        max_occurance = k
        break

print(max_occurance)
