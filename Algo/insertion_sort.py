# Explanation
"""
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

Insertion sort works similarly as we sort cards in our hand in a card game.

We assume that the first card is already sorted then, we select an unsorted card. 
If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. 
In the same way, other unsorted cards are taken and put in their right place.

https://www.youtube.com/watch?v=8oJS1BMKE64
https://www.youtube.com/watch?v=K0zTIF3rm9s

list = [5, 6, 7, 3, 2, 1]
Insertion Sort:
1. Use only nested loop counter to compare adjacent value
2. Use outer loop counter to overcome iteration of nested loop

1st complete loop result: [5, 6, 3, 2, 1, 7] # loop start from 2nd element
2nd complete loop result: [5, 3, 2, 1, 6, 7] # loop start from 3rd element
3rd complete loop result: [3, 2, 1, 5, 6, 7] # loop start from 4th element
4th complete loop result: [2, 1, 3, 5, 6, 7] # loop start from 5th element
5th complete loop result: [1, 2, 3, 5, 6, 7] # loop start from 6th element
6th complete loop result: [1, 2, 3, 5, 6, 7] # loop start from 7th element

NOTE:
1. Use while loop in place of nested loop
2. while loop will run backward from nth to 0 with the condition that main loop val is bigger than inner loop 
3. It will keep the value in its place
4. when the outer loop is completed, the key value will be on right
5. while loop will always sort from nth to 0th in every iteration
"""

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52


# solution
def insertion_sort(l, n):
    for i in range(len(l)):
        val = l[i]
        prev_elem_index = i - 1
        while prev_elem_index >= 0 and l[prev_elem_index] > val:
            l[prev_elem_index + 1] = l[prev_elem_index]
            prev_elem_index = prev_elem_index - 1
        
        l[prev_elem_index + 1] = val

l = [13,46,24,52,20,9]

print(l)
insertion_sort(l, len(l))
print(l)

