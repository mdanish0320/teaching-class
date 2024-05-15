"""
Find the missing number in an array
Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
                    Find the number(between 1 to N), that is not present in the given array.

Example 1:
Input Format:
 N = 5, array[] = {1,2,4,5}
Result:
 3
Explanation: 
In the given array, number 3 is missing. So, 3 is the answer.                    
"""

def missingNumber(a, N):
    # Summation of first N numbers:
    summation = (N * (N + 1)) // 2

    # Summation of all array elements:
    s2 = sum(a)

    missingNum = summation - s2
    return missingNum

def main():
    N = 5
    a = [1, 2, 4, 5]
    # a = [10, 11, 13, 14] <------ x not working
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()