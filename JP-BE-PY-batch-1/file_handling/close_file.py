"""
For the most part, not closing files is a bad idea, for the following reasons:

- It puts your program in the garbage collectors hands - memory leakage
- The data still in memory unless garbage collector hits - memory leakage
- or the most part, many changes to files in python do not go into effect until after the file is closed, so if your script edits, leaves open, and reads a file, it won't see the edits.
- You could, theoretically, run in to limits of how many files you can have open.
- Windows treats open files as locked, so legit things like AV scanners or other python scripts can't read the file.

"""

# write data into the file but cannot read
f = open("data/file_1.txt", "a")
f.write("abcd\n")
f.write("efgh\n")
# f.close()

f = open("data/file_1.txt", "w")
f.write("ijk")
f.close()
