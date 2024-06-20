# class task before starting Dict + loop class

# print multiplication table of 3

# iterate over the list and print "var index:{inddex}, item: {item}"

# cold_drinks = ["pepsi", "marinda", "pakola"]
#check if pakola is there. if found print "pakola is there"
# x = 1

# print("2 x 1 =", (2 * x))
# print("2 x 2 =", (2 * (x + 1)))
# print("2 x 3 =", (2 * (x + 2)))
# print("2 x 4 =", (2 * (x + 3)))
# print("2 x 5 =", (2 * (x + 4)))


# for i in range(1, 21, 2):
#     print("2 x", i,"=", 2 * i)



arr = ["sofa", "chair", "table", "bed", "side-table"]
# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])

arr = ["sofa", "chair", "table", "bed", "side-table", "cub-board", "new_item"]
# i = 0
# print(arr[i]) # sofa

# i += 1
# print(arr[i]) # chair

# i +=1
# print(arr[i]) # table


# for i in range(0, len(arr), 1):
#     print(arr[i])

# # explicit vs implicit

# for i in range(len(arr)):
#     print(arr[i])


# for item in arr:
#     print(item)


cold_drinks = ["pepsi", "marinda", "pakola", "7up", "sprit", "dew"]
#check if pakola is there. if found print "pakola is there"

# print("starting main code")
# for item in cold_drinks:
#     print("finding pakola")
#     if item == "pakola":
#         print("pakola is present")
#         break
# print("running the main code")
    
# finding pakola
# pakola is present

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# for item in arr:
#     if item  == 2 or item == 6 or item == 8:
#         continue

#     print(item)

emails = ["user_1@gmail.com", "user_2@gmail.com", "user_3", "user_4@gmail.com", "admin@gmail.com","user_5", "user_6@gmail.com"]

# send email to all users who has valid email
# send email to only admin

# for item in emails:
#     if "@" not in item: #item.find("@") == -1:
#         continue
#     print("send email to the user", item)

# for item in emails:
#     if item.find("admin")  > -1: #  item.find("admin")  >= 0:
#         print("sending email to admin", item)
#         break

# # data structure dict
# student_detail = ["danish", 30, True, 60.5, None]

# student_detail_mpp = {
#     "name": "danish",
#     "age": "30",
#     "is_employed": "True",
#     "weight": "60.5",
#     "is_student": None
# }

# print(student_detail_mpp)

# student_detail_mpp = {
#     "nameeeeeeeee": "danish",
#     "age": 30,
#     "is_employed": True,
#     "weight": 60.5,
#     "is_student": None
# }

# print(student_detail_mpp)


# print(student_detail_mpp["nameeeeeeeee"])
# # print(student_detail_mpp["is_studentt"])

# student_detail_mpp['weight'] = 70
# student_detail_mpp["have_car"] = True

# print(student_detail_mpp)

# student_detail_mpp["weihgt"] = 70

# print(student_detail_mpp)


# student_detail_mpp = {
#     "nameeeeeeeee": "danish",
#     "age": 30,
#     "is_employed": True,
#     "weight": 60.5,
#     "is_student": None,
#     "siblings": ["fahad", "shoaib", "shahazad"],
#     "employee_detail": {
#         "id": 200,
#         "salary": 5000,
#         "department": "IT",
#         "maganger_of": ["shahzaib", "abdullah", "amin"]
#     }
# }

# print(student_detail_mpp)

# sib = student_detail_mpp["siblings"]
# print(sib[0])

# print(
#     student_detail_mpp["siblings"][0]
# )


employees = [
    {
        "name": "Alice",
        "projects": ["ProjectA", "ProjectB", "ProjectC"],
        "salaries": [70000, 72000, 75000],
        "Department": "HR"
    },
    {
        "name": "Bob",
        "projects": ["ProjectD", "ProjectE", "ProjectF"],
        "salaries": [65000, 67000, 70000],
        "Department": "Finance"
    },
    {
        "name": "Charlie",
        "projects": ["ProjectG", "ProjectH", "ProjectI"],
        "salaries": [80000, 82000, 85000],
        "Department": "IT"
    },
    {
        "name": "Diana",
        "projects": ["ProjectJ", "ProjectK", "ProjectL"],
        "salaries": [75000, 77000, 80000],
        "Department": "Marketing"
    },
    {
        "name": "John",
        "projects": ["ProjectM", "ProjectN", "ProjectO"],
        "salaries": [55000, 57000, 60000],
        "Department": "Sales"
    }
]

print(employees[0]["Department"])
print(employees[1]["Department"])
print(employees[2]["Department"])
print(employees[3]["Department"])
print(employees[4]["Department"])