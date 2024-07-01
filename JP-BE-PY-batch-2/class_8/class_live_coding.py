# file methods
# read()

# r
# w
# a

# print("hello world 1")
# # reading a file
# f = open("book_1.txt", "r")

# data = f.read() # get all file data
# print(data)
# print("hello world 2")


# try:
#     f = open("book_1.txt", "r")
#     data = f.read()
#     print(data)
# except Exception as e:
#     print("exception caught", e)


# readlines()
# f = open("book_1.txt", "r")
# data = f.readlines()
# print(data)

# readline()
# f = open("book_1.txt", "r")
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)


# f = open("book_1.txt", "r")
# data = f.readline()
# while data:
#     print(data)
#     data = f.readline()



# f =  open("book_2.txt", "w+")
# f.write("address 1\n")
# f.write("address 2")

# f.read()
# f.seek(0)


# f = open("book_2.txt", "a")
# f.write("\nfawara chowck")

# write()

# close()
# flush()
# seek()
# tell()


# import traceback
# try:
#     f = open('book_1.txt')
#     s = f.readline()
#     i = int(s.strip())
#     call_the_functio_that_doesnt_exist()
# except OSError as err:
#     print("OS error danish:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     # print(f"Unexpected {err=}, {type(err)=}")
#     # traceback.print_exc()
#     x = traceback.format_exc()
#     print(x)
#     # raise Exception("something went wrong on server")
# finally:
#     print("finally")
   
# print("hellow worl 2")

# Throw error from code
# raise Exception("This is an error")


# class task
# create a file "commentary.txt" using open function
# and add content
# "content 1"

# read file "commentary.txt" and display its contnet

# update file "commentday.txt" and add more content
"content 2"

# Read file "commentary.txt" and use len function
# to see it must have 2 items
# filename = "commentary.txt"

# f = open(filename, "w")
# f.write("cotnet 1\n")
# f.close()


# f = open(filename, "r")
# data = f.read()
# print(data)
# f.close()

# f = open(filename, "a")
# f.write("content 2")
# f.close()

# f = open(filename, "r")
# data = f.readlines()
# print(data, len(data))


# import json
# import pickle

# employees = [
#     {
#      "name": "danish"   
#     },
#     {
#         "name": "Amin"
#     },
#     {
#         "name": "Talha"
#     }
# ]

# print(employees, type(employees))
# # print(employees[0]['name'])
# employee_str = json.dumps(employees)
# print(employee_str, type(employee_str))
# # print(employee_str[0]['name'])

# f = open("employee.txt", "wt")
# f.write(employee_str)

# print(employees, type(employees))
# # print(employees[0]['name'])
# employee_byte = pickle.dumps(employees)
# print(employee_byte, type(employee_byte))
# # print(employee_str[0]['name'])

# f = open("employee.txt", "wb")
# f.write(employee_byte)


# f = open('employee.json', "r")
# data = f.read()

# print(data)
# data = json.loads(data)
# print(data[0]['name'])


# high level vs low level language


# # mutable
# arr = [1, 2, 3, 4]
# print(id(arr))
# arr.append(5)
# print(id(arr))

# print(arr)


# immutable
t = (1, 2, 3, 4)
print(id(t))
t = t + (5,)
print(id(t))

print(t)