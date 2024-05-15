# explanation: https://www.youtube.com/watch?v=YetqNl-E5Zw
# efficient way

l = [1,2,4,7,7,5]
# l = [10, 10, 10]

h = float("-inf")
sh = float("-inf")
for i in range(len(l)):
    if l[i] > h:
        h = l[i]
    elif l[i] > sh and l[i] != h:
        sh = l[i]

print(h, sh)