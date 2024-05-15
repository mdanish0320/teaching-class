l = [1,2,4,7,7,5]

# find the highest number efficient but in 2 loop
h = l[0]
for i in range(len(l)):
    if l[i] > h:
        h = l[i]

sh = l[0]
for i in range(len(l)):
    if  l[i] > sh < h and h != l[i]:
        sh = l[i]

print(h)
print(sh)