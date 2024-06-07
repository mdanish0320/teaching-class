"""
Problem Statement: Given an array, print all the elements which are leaders. 
A Leader is an element that is greater than all of the elements on its right side in the array.
Last element will always be the leader

Example 1:
Input:

 arr = [8, 11, 5, 11, 7, 6, 3]
Output
:
 11, 7, 6 , 3
Explanation:

 Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

 Example 2:
Input:

 arr = [10, 22, 12, 3, 0, 6]
Output:

 22 12 6
"""

arr = [10, 22, 12, 3, 0, 6]
leader = []

for i in range(len(arr)):
    selected_leader = None
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            selected_leader = arr[i]
        else:
            selected_leader = None
            break

    if selected_leader is not None:
        leader.append(selected_leader)

leader.append( arr[len(arr)-1] )
print(leader)