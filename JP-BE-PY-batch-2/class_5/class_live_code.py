# # # list datatype

# # # firsts = "apple, orange, mango, apricot, plum, cherry, strawberry"

# # # fruit_1 = "apple"
# # # first_2 = "orgage"
# # # # .
# # # # .
# # # # .
# # # first_10 = "cherry"

# # # list
# # # syntax: [ ]

# # # list creation
# # firsts_name = ["apple", "orge", "apricate"]
# # soft_drinks = ["pepse", "pakola", "marina"]

# # age_group = [20, 25, 15, 100]

# # student_info = ["danish", 30, True, 60.5, None, ["new_list", "item 2"]]


# # print("firsts_name", firsts_name)
# # print("soft_drinks", soft_drinks)
# # print("age_group", age_group)
# # print("student_info", student_info)

# # # read
# # # items store in the list as location 0, 1, 2, 3, .... n
# # # indexs: 0, 1, 2, 3, ..... n
# # # static data vs dynamic data
# # # declaration vs initialization
# # # python doesn't have declaration syntax

# # print(student_info[0])
# # print(student_info[1])

# # print(student_info[5])
# # # print(student_info[6] # it will raise error "index out of range"



# # print(student_info[5])
# # print(len(student_info))


# # print(
# #     student_info[len(student_info) - 1]
# # )

# # last_element_index = len(student_info) - 1
# # print(
# #     student_info[last_element_index]
# # )

# # print(
# #     student_info[-1]
# # )


# # # update
# # student_info[0] = "fahad"
# # new_name = "faahd"

# # print(student_info)

# # # delete
# # del student_info[0]

# # print(student_info)

# # # slice

# # last_element_index = len(student_info) - 1
# # last_element = student_info[last_element_index] # ["new_list", "item 2"]

# # print(
# #     len(last_element)
# # )

# # last_element[0] = "updated_value"

# # print(student_info)

# # # add new element

# # student_info.append("new_item_1")

# # print(student_info)

# # student_info.pop()

# # print(student_info)

# # list_2 = []

# # print(list_2.extend(student_info))
# # print(list_2)


# # list_3 = ["farhan", "amir", "imran", "anusha", "sameer"]

# # list_3.extend(list_2)

# # print("list_3", list_3)
# # print('list_2', list_2)

# # list_2 = list_2 + list_3

# # print(list_2)




# # # list_2;
# # # list_2 = ["danish"]

# # # sorting
# # student_names = ["farhan", "amir", "imran", "anusha", "farhan", "sameer"]
# # # print(student_names)
# # # print(student_names.sort()) # by default ascening order
# # # print(student_names)

# # # student_names.sort(reverse=True)
# # # print(student_names)

# # # find by vlaue

# # print(
# #     "find by value:",
# #     student_names.index("imran")
# # )

# # # remove by value

# # print(
# #     "remove by value:",
# #     student_names.remove("imran")
# # )
# # print(student_names)


# # # # remove all
# # # print(
# # #     "remove all:",
# # #     student_names.clear()
# # # )
# # # student_names = []
# # # print(student_names)


# # # count duplicate
# # print(
# #     "cound duplicate",
# #     student_names.count("farhan")
# # )
# # # insert at defined position

# # print(
# #     "cound duplicate",
# #     student_names.insert(2, "new student")
# # )

# # print(student_names)

# # class task

# # create a list of juices, add 5 items using append
# # creat a list of cars, add 3 items using insert
# # remove last time from the list ["bed", "table", "chair", "sofa"] using pop and len

# # remove the item "chair" from the list ["bed", "table", "chair", "sofa"] using del and remove

# # furniture = ["bed", "table", "chair", "sofa"]
# # furniture.remove("chair")
# # print(furniture)

# # furniture = ["bed", "table", "chair", "sofa"]
# # chair_index = furniture.index("chair")
# # del furniture[chair_index]

# # slice

# furniture = ["bed", "chair", "table"]

# print(
#     "pepsi" in furniture
# )
# # value in list

# print(
#     "Chair" in furniture
# )

# # "C" != "c" # case sensitive


# # slice
# # syntax: varibale[start_from : till]
# # exclusive vs inclusive

# car_list = ["corolla", "mehran", "cultus", "aqua", "civic", "vitz", "alto"]
# print(car_list)
# print(car_list[0:2])

# print(car_list[2:5])

# print(car_list[:3])
# print(car_list[3:])

# x = "hello world"
# print(x[4:10])

# print("helloo" in "hello world")

# student_detail_str = "danish, 30, 60.5, True"
# detail_list = student_detail_str.split(",")

# print(detail_list)

# print(
#     "--".join(detail_list)
# )

# loop
# students = ["dansh", "imran", "huzefa", "abdullah", "marij"]

# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])


# for x in ["dansh", "imran", "huzefa", "abdullah", "marij"]:
#     print(x)
    
students = ["dansh", "imran", "huzefa", "abdullah", "marij"]    
# for x in students:
#     print(x)
    

# print(
#     list(range(10))
# )

# print(
#     range(len(students))
# )


for item in ["dansh", "imran", "huzefa", "abdullah", "marij"]:
    print(item)

students = ["dansh", "imran", "huzefa", "abdullah", "marij"]    
for i in range(len(students)): # [0, 1, 2, 3, 4]
    print(students[i])
    


furtniture = ["bed", "table", "chair", "sofa"]

# loop over furniture
# check if chair exists or not``