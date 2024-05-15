# Explanation
"""
Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.

Here, a problem is divided into multiple sub-problems. Each sub-problem is solved individually. Finally, sub-problems are combined to form the final solution.

https://www.youtube.com/watch?v=ZRPoEKHXTJg
https://www.youtube.com/watch?v=nCNfu_zNhyI


"""
def find_min_index():
    pass

# solution
def selection_sort(list_a):
    for i in range(len(list_a)):
        min_index = i
        for j in range(i, len(list_a)):
            if list_a[min_index] < list_a[j]:
                min_index = j
        
        list_a[min_index], list_a[i] = list_a[i], list_a[min_index]

    

l = [3, 1, 2, 10, 5, 4]
selection_sort(l)
print(l)


