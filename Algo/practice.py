# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52


# solution
# def bubble_sort(l):
#     for i in range(len(l)):
#         for j in range(len(l) - i  - 1):
#             if l[j] < l[j + 1]:
#                 l[j], l[j+1] = l[j+1], l[j]



# solution
def insertion_sort(l):
    for i in range(len(l)):
        val = l[i]
        prev_ele_index = i - 1
        while prev_ele_index >= 0 and val > l[prev_ele_index]:
            l[prev_ele_index + 1] = l[prev_ele_index]
            prev_ele_index -= 1
        l[prev_ele_index + 1] = val 


l = [13,46,24,52,20,9]

print(l)
insertion_sort(l)
print(l)










