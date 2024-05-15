def missingNumber(a, N):
    hash = [0] * (N + 1)  # hash array

    # storing the frequencies:
    for i in range(N - 1):
        hash[a[i]] += 1

    # checking the frequencies for numbers 1 to N:
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5] 
    
    # a = [10, 11, 13, 14] <----- x is not working 
    
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()