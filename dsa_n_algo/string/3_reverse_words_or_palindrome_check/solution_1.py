"""
Problem Statement: Given a string s, reverse the words of the string.

Examples:

Example 1:
Input: s=”this is an amazing program”
Output: “program amazing an is this”

Example 2:
Input: s=”This is decent”
Output: “decent is This”
"""

_input = "this is an amazing program"
arr = _input.split(" ")
new_arr = []
for i in range(len(arr) -1, -1, -1):
    new_arr.append(arr[i])

print(new_arr)