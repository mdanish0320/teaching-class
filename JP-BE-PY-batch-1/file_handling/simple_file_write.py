# write string data in file
f = open("data/file_w.txt", "w")

f.write("A B C D\n")
f.write("E F G H")
f.close()


# write list of str in file
f = open("data/file_w.txt", "w")
f.writelines(["ABCD\n", "EFGH\n"])
f.writelines("IJKL")
f.close()

