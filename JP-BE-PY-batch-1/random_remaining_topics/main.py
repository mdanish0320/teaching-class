# topic slice

# syntax
# variable[:::]
# start: end: jump just like range function

# slice function will work on sequence data type only whose element are accessable by index
# i.e
# string
# list
# tuple

# x = "hello world" # sequence data time
# l = [1, 2, 3, 4, 5, 6, 7 ,8 , 9, 10, 11]
# t = (1, 2, 3, 4, 5, 6, 7 ,8 , 9, 10, 11)

# chars = x[3:10] 
# print(chars) # lo world

# l1 = [1, 2, 3, 4, 5, 6, 7 ,8 , 9, 10, 11]
# print(l1[0:5])  # [1, 2, 3, 4, 5]
# print(l1[5:10]) # [6, 7 ,8 , 9, 10]
# print(l1[2:])   # [3, 4, 5, 6, 7 ,8 , 9, 10, 11]]
# print(l1[:5])   # [0, 1, 2, 3, 4]
# print(l1[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1]


# Topic: Sring method split -> break string into list
# x = "hello world"
# print(x.split(" ")) # ["hello", "world"]

# x = "m.danirous@gmail.com"
# print(x.split("@")) # ["m.danirous", "gmail.com"]


# Topic: String method join -> create string from list

# words = ["This", "is", "a", "sample"]
# sentens = " ".join(words)
# print(sentens)
