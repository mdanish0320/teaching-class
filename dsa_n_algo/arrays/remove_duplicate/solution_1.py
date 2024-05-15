"""
Remove Duplicates in-place from Sorted Array
"""

l = [1,1,2,2,3,3]

s = set()

for val in l:
    s.add(val)

print(s)

# OR

print(
    set(l)
)