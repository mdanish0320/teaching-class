l = [1,1,2,2,3,3]
l2 = []

# selection sort algorithm
# take one element from outer loop
# compare select element to all remaining element using inner loop
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] == l[j]:
            l2.append(i)
            continue

# sort by descending is necessary
# otherwise after deletion list gets resized and encouter the error index out of range
# therefore we will delete the largest index first
for i in sorted(l2, reverse=True):
    del l[i]

print(l)

