# CRUD Operations

# We use dict (object) in order to add multiple information of a single item
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023"
}
print(d)

# how to access specified item in the dict
print(d['name'])
print(d['gender'])
print(d['xyz']) # error because the kye "xyz" doesn't exists


# create a nested dict
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023",
    "employee_info": {
        "id": 1,
        "joining_date": "2000"
    }
}

# access item in a nested dict
nested_d = d['employee_info']
print(nested_d)
print(nested_d['id'])
print(d['employee_info']['id']) # or access directly from a variable d


# len will only work to count the number of items in root level
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023",
    "employee_info": {
        "id": 1,
        "joining_date": "2000"
    }
}
# it will return 4 and not 6. It will not count the elements inside employee_info
print(len(d))


# update item in the dict
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023",
    "employee_info": {
        "id": 1,
        "joining_date": "2000"
    }
}
d['name'] = "Sidra"
d['gender'] = "female"
print(d['name'])
print(d['gender'])
