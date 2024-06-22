# dictionary common methods
dictt = {
    "danish": 200,
    "fahad": 400,
    "shoaib": 600,
    "books": ["1", "2", "3"]
}

# display all keys of the dict in the form of list
print(dictt.keys())

# display all values of the dict in the form of list
print(dictt.values())

# display all keys and values of the dict in the form of tuple
print(dictt.items())

# iterate over the dict using .items() method
for key, val in dictt.items():
    print(key, "=>", val)
    
# update dict using update method
dictt['books'] = ["1", "2", "3", "4"]
dictt.update({"books": ["1", "2", "3", "4"]})
print(dictt)