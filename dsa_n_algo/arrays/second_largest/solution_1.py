l = [1,2,4,7,7,5]
l = list(set(l)) # this is the issue in sorting solution, the duplicate hightest number

# bubble sort
for i in range(2):
    for j in range(len(l) - 1):
        if l[j] > l[j+1]:
            l[j], l[j+1]= l[j+1], l[j]

print(l[-2]) 



