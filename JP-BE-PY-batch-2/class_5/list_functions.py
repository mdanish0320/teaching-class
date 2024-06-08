student_info = ["danish", 30, True, 60.5, None, ["new_list", "item 2"]]

# add new element
student_info.append("new_item_1")
print(student_info)

# delete last element
student_info.pop()
print(student_info)

# merge 2 lists
# example 1
list_2 = []
print(list_2.extend(student_info))
print(list_2)

# example 2
list_3 = ["farhan", "amir", "imran", "anusha", "sameer"]
list_3.extend(list_2)

print("list_3", list_3)
print('list_2', list_2)

# example 3
list_2 = list_2 + list_3
print(list_2)



# sorting in ascending order
student_names = ["farhan", "amir", "imran", "anusha", "farhan", "sameer"]
print(student_names)
print(student_names.sort()) # by default ascening order
print(student_names)

# sorting in descending order
student_names.sort(reverse=True)
print(student_names)


# find element index by vlaue
print(
    "find by value:",
    student_names.index("imran")
)

# remove element by value
print(
    "remove by value:",
    student_names.remove("imran")
)
print(student_names)


# remove all
print(
    "remove all:",
    student_names.clear()
)
student_names = []
print(student_names)


# count number of occurances of the value
print(
    "cound duplicate",
    student_names.count("farhan")
)

# insert at defined position
print(
    "cound duplicate",
    student_names.insert(2, "new student")
)

print(student_names)