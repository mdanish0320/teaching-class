"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


arr = ["flower","flow","flight"]

lst = []
for i in range(len(arr)):
    smaller_element = arr[i]
    for j in range(i+1, len(arr)):
        common_prefx_len = 0
        if len(arr[j]) < len(smaller_element):
            smaller_element = arr[j]
        char_a = arr[i]
        char_b = arr[j]
        for cnt in range(len(smaller_element)):
            if char_a[cnt] == char_b[cnt]:
                common_prefx_len += 1
    lst.append(common_prefx_len)

print(min(lst))
print(lst)