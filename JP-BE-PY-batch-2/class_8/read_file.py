# three methods to read the file

# read
# readlines
# readline

# read whole file as text
# it will raise error if file dones't exists
f = open("book_1.txt", "r")
content_size = 100
data = f.read(content_size) # get all file data
f.close()
print(data)


# read whole file as a list
f = open("book_1.txt", "r")
data = f.readlines() # get all file data
f.close()
print(data)


# read only 1 line from the file
# memory efficient code
f = open("book_1.txt", "r")
data = f.readline() # get all file data
f.close()
print(data)

# read whole file line by line
# memory efficient code
f = open("book_1.txt", "r")
data = f.readline()
while data:
    print(data)
    data = f.readline()
f.close()
