# Explanation
"""
Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration 
and places that element at the beginning of the unsorted list.

https://www.youtube.com/watch?v=92BfuxHn2XE
https://www.youtube.com/watch?v=hhkLdjIimlw

list = [5, 6, 7, 3, 2, 1]
Selection Sort:
1. Take the first element [0]th and compare it to all the elements in the list
2. During comparison, if found the smaller number than the [0]th, update the index and continue the loop with comparing with new index i.e list = [5, 6, 7, 3, 2, 1]
    a. First compare [0]th index (5) to all the elements of the list
    b. During the 3rd iteration, loop encounters the value 3 at the index [3] which the < than the value 5
    c. Update index: [3]th. Now continue the loop and compare the [3]th index to the remaining values of the list
3. When the outer loop iteration completed, we will have the index of the smallest integer of the list


1st complete loop result: [1, 5, 6, 7, 3, 2] # loop start from 2nd element
2nd complete loop result: [1, 2, 5, 6, 7, 3] # loop start from 3rd element
3rd complete loop result: [1, 2, 3, 5, 6, 7] # loop start from 4th element
4th complete loop result: [1, 2, 3, 5, 6, 7] # loop start from 5th element
5th complete loop result: [1, 2, 3, 5, 6, 7] # loop start from 6th element
6th complete loop result: [1, 2, 3, 5, 6, 7] # loop start from 7th element

NOTE:
1. Number of iteration gets smaller after each complete loop
2. Outer loop + Nested loop
3. Inner loop iteration gets smaller
4. It insert the hightest/smallest value at the first index
5. Nested Loop always gonna start outerloop selection + 1
"""


# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

# solution:

def selection_sort(l, n):
    for step in range(len(l)):
        smallest_index = step
        for n in range(step + 1, len(l)):
            if l[smallest_index] > l[n]:
                smallest_index = n
        l[step], l[smallest_index] = l[smallest_index], l[step]



l = {13,46,24,52,20,9}
l = list(l)

print(l)
selection_sort(l, len(l))
print(l)

