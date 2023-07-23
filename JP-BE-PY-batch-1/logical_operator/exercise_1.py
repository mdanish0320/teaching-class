a = True
b = True
c = False
d = False


print(a and b)
print(a or b)
print(a or c)
print(a and d)
print(a and b or c)

# wrong answer for all students
print(a or b and c)

# use round bracket to set priority
print((a or b) and c)
print(a or (b and c))
