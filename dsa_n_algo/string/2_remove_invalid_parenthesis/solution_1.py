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

_input = "()()(()"
# _input = "()()(()"
# _input = "(a)())()"
# _input = "()()(((()"
arr = []
_open = 0
for i in _input:
    
    if i == "(":
        _open += 1
    elif i == ")":
        _open -= 1


    if (_open == 1 and i == "(") or (_open == 0 and i == ")") or i not in ["(", ")"]:
        arr.append(i)
    else:
        if _open > 0:
            _open -= 1
        else:
            _open += 1
        
print("".join(arr))
