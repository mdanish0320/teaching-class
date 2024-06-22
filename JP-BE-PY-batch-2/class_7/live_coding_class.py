# dictionary common methods
dictt = {
    "danish": 200,
    "fahad": 400,
    "shoaib": 600,
    "books": ["1", "2", "3"]
}

# # print(dictt.keys())
# # print(dictt.values())
# # print(dictt.items())

# for key, val in dictt.items():
#     print(key, "=>", val)
    
# dictt['books'] = ["1", "2", "3", "4"]
# dictt.update({"books": ["1", "2", "3", "4"]})
# print(dictt)




# loop using enumerate on list and dict
arr = [100, 200, 300, 400, 500]

# for i in range(len(arr)):
#     print(i, arr[i])


# for i, val in enumerate(arr):
#     print(i, val)
    
# for i, (key, value) in enumerate(dictt.items()):
#     print(i, key)

students = ["alice", "bob", "charlie"]
score = [80, 90, 100]

dictt = {
    "students": [],
    "score": []
}

# zip function: loop over multiple list

for i, val in enumerate(students):
    dictt["students"].append(students[i])
    dictt["score"].append( score[i])
        

for i in arr:
    pass    

# loop will run forever
# while True:
#     print("hello world")

# x = 1
# while x > 0 and x <= 10:
#     print("hello world")


# x = 1
# while x > 0 and x <= 10:
#     x += 1
#     print("hello world")

# x = 10
# while False:
#     print("hello world")

# x = 10
# while x > 0:
#     x -= 1
#     print("hello world")
    
    
    
# ask user input postive number and keep asking positive number and display   
# terminate the program when user input negative number 

# user_number = int(input("enter positive number"))
# while user_number > 0:
#     print(user_number)
#     user_number = int(input("enter positive number"))


# while True:
#     user_number = int(input("enter positive number"))    
#     if user_number < 0:
#         break
#     print(user_number)

# list_1 = [10, 20, 30]
# list_2 = [40, 50, 60, 30]

# for item_1 in list_1:
#     for item_2 in list_2:
#         if item_1 == item_2:
#             print("common number is", item_1)
            
            
"New York, California, China"

order_1_item_1 = "laptop"
order_1_destination = "China"

# if order_1_destination == "New York":
#     shipment_price = 10
# elif order_1_destination == "California":
#     shipment_price = 20
# elif order_1_destination == "China":
#     shipment_price = 30
# print(shipment_price)


# order_1_destination = "New York"

# if order_1_destination == "New York":
#     shipment_price = 10
# elif order_1_destination == "California":
#     shipment_price = 20
# elif order_1_destination == "China":
#     shipment_price = 30
# print(shipment_price)


# order_1_destination = "China"

# if order_1_destination == "New York":
#     shipment_price = 10
# elif order_1_destination == "California":
#     shipment_price = 20
# elif order_1_destination == "China":
#     shipment_price = 30
# print(shipment_price)


# locations = ["New York", "California", "China"]

# shipment_price = 0
# for loc in locations:
#     if loc == order_1_destination:
#         shipment_price = 10
#     elif loc == order_1_destination:
#         shipment_price = 20
#     elif loc == order_1_destination:
#         shipment_price = 30
   
# print(shipment_price)



# def get_shipping_price():
#     for loc in locations:
#         if loc == order_1_destination:
#             shipment_price = 10
#         elif loc == order_1_destination:
#             shipment_price = 20
#         elif loc == order_1_destination:
#             shipment_price = 30
            

# get_shipping_price()

# local vs global

# def multiply():
#     global x
#     print("hello world")
#     # print(x * y)
   
#     x = 100
#     print(x)

# x = 2
# y = 5

# # print( x * y)
# print(x)

# multiply()

# print(x)

# x  = 100
# y = 100

# x = "hello"

# def modify_string(xx): # calle
#     print(xx)
#     xx = xx + " world"
#     print(xx)
#     return xx

# x = modify_string(x) # caller
# print(x)

# impure function vs pure function

# def get_shippment_price(order_1_destination):
#     if order_1_destination == "New York":
#         shipment_price = 10
#     elif order_1_destination == "California":
#         shipment_price = 20
#     elif order_1_destination == "China":
#         shipment_price = 30
#     print(shipment_price)
#     return shipment_price

# def calculate_overall_order_tax(total_price, shipment_rate):
#     pass

# shipment_price = get_shippment_price("China")
# calculate_overall_order_tax(1000, shipment_price)
    
# arr = [1, 2, 3, 4]

# x = arr.sort()
# print(x)


# def print_invoice():
#     asfds
#     adsfdsaf
#     adsfdsaf
#     adsfdsaf
#     adsfdsaf
#     adsfdsaf
#     return 


x = 5
y = 5

def do_sum(*abc):
   print(abc)
    

do_sum(1, 2, 3, 4, 5,6 ,7 ,8)