"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

video: https://www.youtube.com/watch?v=-zSxTJkcdAo
s = "cadbzabcd"
"""

s = "pwwkew"

res = ""
max_ss = 0
for i in s:
    res = ""
    max_ss = 0
    repeat_found = False

    for j in s:
        if j not in res:
            res += j
        else:
            break

    if max_ss < len(res):
        max_ss = len(res)
print(res)
print(max_ss)