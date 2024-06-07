"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a)()()"]
"""

# _input = "()()(()"
# _input = "()())()"
_input = "(a)())()"
# _input = "()()(((()"
arr = []
_open = 0

for c in _input:
    if c == "(":
        arr.append(c)
        _open += 1
    elif c == ")" and _open > 0:
        arr.append(c)
        _open -= 1
    elif c != ")":
        arr.append(c)
    
filtered = []
for c in arr[::-1]:
    if c == "(" and _open > 0:
        _open -= 1
    else:
        filtered.append(c)


print("".join(filtered[::-1]))