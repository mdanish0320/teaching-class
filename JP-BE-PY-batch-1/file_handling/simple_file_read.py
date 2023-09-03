# read a file using read method
f = open("data/file_r.txt", "r")
content = f.read() # read whole file at once and return content as string
print(type(content))  # <class str>
print(content)


# read a file using readlines method
f = open("data/file_r.txt", "r")
content = f.readlines() # read whole file at once and return content as list separated by new lines
print(type(content)) # <class list>
for elem in content:
    print(elem)
    
# read a file using readline method - memory efficient
f = open("data/file_r.txt", "r")
row  = f.readline() # return a single line from file
print(row)
row = f.readline()  # return the next single line from file
print(row)

# read whole file line by line efficiently
f = open("data/file_r.txt", "r")
myline = f.readline()
while myline:
    print(myline)
    myline = f.readline()
    
f.close()
