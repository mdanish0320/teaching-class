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

str_1 = "foo"
str_2 = "bar"

mapp_1 = {}
mapp_2 = {}

for i in range(len(str_1)):
    char_str_1 = str_1[i]
    char_str_2 = str_2[i]
    
    if mapp_1.get(char_str_2) is None:
        mapp_1[char_str_2] = str_1[i]
    
    if mapp_2.get(char_str_1) is None:
        mapp_2[char_str_1] = str_2[i]

res = ""
for char in str_2:
    res += mapp_1[char]

res_2 = ""
for char in str_1:
    res_2 += mapp_2[char]

if res == str_1 and res_2 == str_2:
    print("isomorphic")
else:
    print("no")