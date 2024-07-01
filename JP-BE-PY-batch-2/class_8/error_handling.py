# 3 types of error
# run time
# compile time
# logical

import traceback
try:
    f = open('book_1.txt')
    s = f.readline()
    i = int(s.strip())
    call_the_functio_that_doesnt_exist()
except OSError as err:
    print("OS error danish:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    # traceback.print_exc()
    x = traceback.format_exc()
    print(x)
finally:
    print("finally")


# raise custom error
raise Exception("This is my error")


# Built-in Exception Types
# https://www.w3schools.com/python/python_ref_exceptions.asp
