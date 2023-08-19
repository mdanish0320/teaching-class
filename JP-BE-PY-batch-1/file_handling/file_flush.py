# file handling method flush
import time

f = open("data/file_flush.txt", "w")

for i in range(1, 60):
    print("write line", i)
    f.write("line" + str(i) + "\n")
    if i % 10 == 0:
        print("flushed")
        f.flush()
    time.sleep(1) # num of seconds

f.close()
