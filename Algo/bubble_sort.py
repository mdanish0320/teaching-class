# Explanation
"""
Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order.

https://www.youtube.com/watch?v=Cq7SMsQBEUw
https://www.youtube.com/watch?v=ppmIOUIz4uI

list = [5, 6, 7, 3, 2, 1]
Bubble Sort:
1. Use only nested loop counter to compare adjacent value
2. Use outer loop counter to overcome iteration of nested loop

1st complete loop result: [5, 6, 3, 2, 1, 7] # loop start from 2nd element
2nd complete loop result: [5, 3, 2, 1, 6, 7] # loop start from 3rd element
3rd complete loop result: [3, 2, 1, 5, 6, 7] # loop start from 4th element
4th complete loop result: [2, 1, 3, 5, 6, 7] # loop start from 5th element
5th complete loop result: [1, 2, 3, 5, 6, 7] # loop start from 6th element
6th complete loop result: [1, 2, 3, 5, 6, 7] # loop start from 7th element

NOTE:
1. Number of iteration gets smaller after each complete loop
2. Outer loop + Nested loop
3. Inner loop iteration gets smaller
4. It insert the hightest/smallest value at the last index
5. Nested Loop always gonna start from index one
"""

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52


# solution
def bubble_sort(l, n):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
        


l = [13,46,24,52,20,9]

print(l)
bubble_sort(l, len(l))
print(l)
