# nested loop
for i in [1, 2, 3, 4]:
    print("first loop", i)
    for j in [50, 60, 70, 80]:
        print("nested loop", j)
        
# first loop 1
# nested loop 50
# nested loop 60
# nested loop 70
# nested loop 80
# first loop 2
# nested loop 50
# nested loop 60
# nested loop 70
# nested loop 80
# first loop 3
# nested loop 50
# nested loop 60
# nested loop 70
# nested loop 80
# first loop 4
# nested loop 50
# nested loop 60
# nested loop 70
# nested loop 80


for i in range(1, 5):
    for j in range(i):
        print(i, end="") # note: printing i and not j and use end="" for one line print
    print() # for line break

# 1
# 22
# 333
# 4444

# read this blog to learn and understand creating more shapes using nested loop
# https://ashaicy99.medium.com/python-nested-for-loops-practice-exercises-dee4e76a00bb
# https://www.cs.utexas.edu/users/scottm/cs305j/handouts/slides/Topic6NestedForLoops_4Up.pdf
