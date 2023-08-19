# importing the module
import tracemalloc

# code or function for which memory
# has to be monitored


def app():
    f = open("data/16-mb-file.csv")
    str_content = f.read()
    # list_content = f.readlines()
    
    # row_1 = f.readline()
    # row_2 = f.readline()
    # row_3 = f.readline()
    
    # myline = f.readline()
    # while myline:
    #     myline = f.readline()
    # f.close()


# starting the monitoring
tracemalloc.start()

# function call
app()

# displaying the memory
current, peak  = tracemalloc.get_traced_memory()

memory_size_in_mb = peak/(1024*1024)
print(memory_size_in_mb, "mb")

# stopping the library
tracemalloc.stop()
