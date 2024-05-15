# Explanation
"""
Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.

Here, a problem is divided into multiple sub-problems. Each sub-problem is solved individually. Finally, sub-problems are combined to form the final solution.

https://www.youtube.com/watch?v=ZRPoEKHXTJg
https://www.youtube.com/watch?v=nCNfu_zNhyI


"""

# solution

def merge_sort(l):
    if len(l) <= 1:
        return l
    
    mid =  len(l)//2
    left = l[:mid]
    right = l[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_arr(left, right)

def merge_two_arr(arr1, arr2):
    sorted_list = []
    len_a = len(arr1)
    len_b = len(arr2)
    i = j = 0

    while i < len_a and j < len_b:  # if both array contains data
        if arr1[i] <= arr2[j]:      # find which array is larger
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1
    
    # above loop will process only same number of items in both array
    # if arr1 contains 5 elements and arr2 contains 7
    # then above loop will run only 5 iteration
    
    # below while loop is necessary to process remaining 2 elements
     
    while i < len_a:                # add remaining items of the list
        sorted_list.append(arr1[i])
        i += 1

    while j < len_b:                # add remaining items of the list
        sorted_list.append(arr2[j])
        j += 1    

    return sorted_list

l1 = [5,8,12, 56]
l2 = [7,9, 45, 51]

# x = merge_two_arr(l1, l2)
# print(x)

l = [5, 7, 8, 9, 12, 45, 51, 56]
sorted_list = merge_sort(l)
print(sorted_list)


