"""
Example 1:
Input:
 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output:
 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation:
 All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
"""

# selection sort
# similar to the solution of "remove duplicate elements from list"
# lst = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
lst = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

i = 0
for j in range(len(lst)):
    if lst[j] != 0:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1

print(lst)