"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

arr = [3,3,3,1,2,1,1,2,3,3,4]
"""

arr = [1,2,3,2,2]
k = 2

# l = 0
# mpp = set()
# max_trees = 0
# for r in range(len(arr)):
#     print(r, l, mpp)
#     while arr[r] not in mpp and len(mpp) >= k:
#         print("remove", arr[l])
#         mpp.remove(arr[l])
#         l += 1

#     mpp.add(arr[r])
#     max_trees = max(max_trees, r - l + 1)

# print(max_trees)


basket = {}
left = 0
max_fruits = 0

for right in range(len(arr)):
    if arr[right] in basket:
        basket[arr[right]] += 1
    else:
        basket[arr[right]] = 1

    while len(basket) > k:
        basket[arr[left]] -= 1
        if basket[arr[left]] == 0:
            del basket[arr[left]]
        left += 1

    max_fruits = max(max_fruits, right - left + 1)
print(max_fruits)
