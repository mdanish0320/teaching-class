"""
Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. 
You may consider that such an element always exists in the array.

Example 1:
Input Format
: N = 3, nums[] = {3,2,3}
Result
: 3
Explanation
: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 
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