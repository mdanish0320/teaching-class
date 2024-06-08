# read
# items store in the list as location 0, 1, 2, 3, .... n
# indexs: 0, 1, 2, 3, ..... n
student_info = ["danish", 30, True, 60.5, None, ["new_list", "item 2"]]

print(student_info[0])
print(student_info[1])

print(student_info[5])
# print(student_info[6] # it will raise error "index out of range"


print(student_info[5])
print(len(student_info))


print(
    student_info[len(student_info) - 1]
)

last_element_index = len(student_info) - 1
print(
    student_info[last_element_index]
)

print(
    student_info[-1]
)