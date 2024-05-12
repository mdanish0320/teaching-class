# print syntax with extra features is given below: 
# print("text", sep=separator, end=end)

# this will print hello and world in 2 different lines. Why?
print("hello")
print("world")

# this will also print hello and world in 2 different lines. Why?
print("hello"); print("world")

# because print have default value of the argument end i.e end="\n" i.e
print("hello", end="\n")
print("world", end="\n")

# we can change this behavour.
print("hello", end="-") # hello-
print("world", end="-") # world-


#--------------------------------#
#--------------------------------#
# the blow command will display "hello world" with space, why?
print("hello", "world")

# because print have default value of the argument sep i.e sep=" " i.e
print("hello", "world", sep=" ")

# we can change this behavour i.e
print("hello", "world", sep=",") # hello,world
print("hello", "world", sep=":") # hello:world
print("hello", "world", sep="--") # hello--world