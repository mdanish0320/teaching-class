# write and read the file
f = open("data/file_w_r.txt", "w+")

print("pointer position: ", f.tell()) # pointer position 0

f.write("1234")

print("pointer position: ", f.tell()) # pointer position 4

f.seek(0) # set pointer position to 0

print("pointer position: ", f.tell()) # pointer position 0

content = f.read()

print(content)



# read and write the file
f = open("data/file_r_w.txt", "r+")

print("pointer position: ", f.tell()) # pointer position 0

f.read()

print("pointer position: ", f.tell()) # pointer position > 0

f.seek(0) # set pointer position to 0

print("pointer position: ", f.tell()) # pointer position 0

f.write("abcd") # remove all previous data of file

print("pointer position: ", f.tell())  # pointer position 4




# read and append data into the file
f = open("new_file_a.txt", "a+")

print("pointer position: ", f.tell())  # pointer position  > 0 if data already exists

f.seek(0)  # set pointer position to 0

content = f.read()

print("pointer position: ", f.tell())  # pointer position  > 0

print(content)

