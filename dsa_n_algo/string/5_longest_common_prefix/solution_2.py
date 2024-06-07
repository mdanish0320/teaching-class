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




def test():
    arr = ["flower","flow","flight"]
    first_element = arr[0]
    res = ""

    for i in range(len(first_element)):
        for word in arr:
            print(i, word)
            if i == len(word) or first_element[i] != word[i]:
                return res
        res += arr[0][i]

ans = test()

print(ans)