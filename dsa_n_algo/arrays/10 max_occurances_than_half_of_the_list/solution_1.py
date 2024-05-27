"""
Count Maximum Consecutive One's in the array

Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

Example 1:

Input: prices = {1, 1, 0, 1, 1, 1}

Output: 3

Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

"""

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    for i in range(n):
        # Selected element is arr[i]
        cnt = 0
        for j in range(n):
            # Counting the frequency of arr[i]
            if arr[j] == arr[i]:
                cnt += 1

        # Check if frequency is greater than n/2
        if cnt > (n // 2):
            return arr[i]

    return -1

arr = [2,2,1,1,1,2,2,2, 3]
ans = majorityElement(arr)
print("The majority element is:", ans)