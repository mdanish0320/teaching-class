"""
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"

Output: 3
"""

s = "()(())((()()))"

cnt = 0
max_depth = 0
for char in s:
    if char == "(":
        cnt += 1
        if cnt > max_depth:
            max_depth = cnt
    if char == ")":
        cnt -= 1

print(max_depth)