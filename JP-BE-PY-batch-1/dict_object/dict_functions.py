# add new item in a dict using update method
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023"
}
d.update({"id": 400}) # it will add a new item in a dict "d" if given key doesn't exist
print(d)


# access item in a dict "d" using get method
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023"
}
d.get("name") # danish
d.get("xyz")  # None -> since the key 'xyz' doen't exist, get method will return None
d.get("xyz", "optional value")  # the value specified in 2nd parameter will return if key 'xyz' doesn't exist


# update item in a dict using update method
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023"
}
d.update({"name": "fahad"})  # it will change the value if the key "name" exists
print(d)


# delete an item from a dict
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023"
}

del d['name']
print(d) 


# delete all items from a dict
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023"
}
# d.clear()
d = {}
print(d)


# display all the keys of the dict
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023"
}
d.keys() # name, gender, date_of_birth


# display all the value of the dict
d = {
    "name": "danish",
    "gender": "male",
    "date_of_birth": "2023"
}
d.keys()  # danish, male, 2023


# how to merge 2 dicts
d1 = {"a": 1, "b": 2, "c": 3} # req
d2 = {"d": 4, "e": 5, "f": 6} # fetched from db

# d3 = d1 | d2 # this syntax is not working on python 3.6
d3 = {**d1, **d2}
print(d3)
