# l = [1,2,4,7,7,5]
# l = [1,2,3,4,5,6]
l = [5,4,3,2,1]

# bubble sort algorithm
for i in range(len(l)):
    is_sorted = True
    for j in range(len(l) - 1):
        if l[j] > l[j+1]:
            is_sorted = False
    if is_sorted == True:
        break
print(is_sorted)
    