# CRUD Operations

# We use list (array) in order to add multiple items in a variable i.e
l = ["pizza", "burger", "sandwich", "bbq"]
print(l)


# how to access 1 item from the list
l = ["pizza", "burger", "sandwich", "bbq"]
item_1 = l[0]
print(item_1) # pizza
item_2 = l[1]
print(item_2) # burger
item_3 = l[2]
print(item_1) # sandwich
item_4 = l[3]
print(item_2) # bbq

item_5 = l[4] # it will produce an error: index out of range



# how to count items in a list
l = ["pizza", "burger", "sandwich", "bbq"]
total_items = len(l)
print(total_items) # 4


# how to access last item of the list - 1
l = ["pizza", "burger", "sandwich", "bbq"]
total_items = len(l)
last_item = l[total_items - 1]
print(last_item) # bbq

# how to access last item of the list - 2
l = ["pizza", "burger", "sandwich", "bbq"]
last_item = l[-1]
print(last_item) # bbq


# how to update item in a list
l = ["pizza", "burger", "sandwich", "bbq"]
print(l) # ["pizza", "burger", "sandwich", "bbq"]
l[0] = 'anda-paratha'
print(l) # ["anda-paratha", "burger", "sandwich", "bbq"]