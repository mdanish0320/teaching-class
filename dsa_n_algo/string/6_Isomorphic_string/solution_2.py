"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

video exmplanation: https://www.youtube.com/watch?v=7yF-U1hLEqQ
"""

str_1 = "egg"
str_2 = "add"

def test():
    mapp_1, mapp_2 = {}, {}
    for i in range(len(str_1)): # for c1, c2 in zip(str_1, str_2) because both have the same length
        c1, c2 = str_1[i], str_2[i]
        if (c1 in mapp_1 and mapp_1[c1] != c2) or (c2 in mapp_2 and mapp_2[c2] != c1):
            return False
        mapp_1[c1] = c2
        mapp_2[c2] = c1

    return True

res = test()

print(res)