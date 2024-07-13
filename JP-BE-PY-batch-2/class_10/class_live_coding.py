# local vs global variable
# x = 100

# def sum():
#     y  = 200
#     print(y)
    
# print(y)


# def increment():
#     counter = 0
#     counter += 1
#     print(counter)

# counter = 100
# def increment():
#     counter = 300
#     print(counter)
    
# increment()
# increment()
# increment()

# object oriented Programming

# class ColdDrink: # passcal case
#     # class attributes
#     height = 100
#     color = "black"
#     taste = "salty"
#     body = "plastic"
    
    

# print(ColdDrink.color)
# ColdDrink.color = 200

# pepsi = ColdDrink()
# print(pepsi.color)

# pepsi = ColdDrink()
# pepsi_2 = ColdDrink()
# pepsi_3 = ColdDrink()


# print(pepsi.color)
# pepsi.color = "white"
# print(pepsi.color)

# print("pepsi_3", pepsi_3.color)


# pepsi_4 = ColdDrink()
# print("pepsi_4", pepsi_4.color)
        
# class Employee: # passcal case
#     # class attributes
#     bonus_amount = 10
#     def __init__(self, _id, _name, _salary):
#         # instance attributes
#         self.id = _id
#         self.name = _name
#         self.salary = _salary
    
#     def get_tax_amount(self):
#         return float(self.salary) * 0.1
    
#     # behavour
#     def get_salary(self):
#         tax_amount = self.get_tax_amount()
#         return self.salary - tax_amount
        
    
        
# talha = Employee(1, "talah", 100)
# danish = Employee(2, "danish", 200)

# print(talha.bonus_amount, danish.bonus_amount)
# talha.bonus_amount = 30
# Employee.bonus_amount = 20
# print(talha.bonus_amount, danish.bonus_amount)

# print(talha.get_salary(), talha.salary)


    
"""
Write a Python program to create a person class. 
Include attributes like name, country and date of birth. 
Implement a method to determine the person's age.
"""

# from datetime import datetime, date

# class Person:
#     # dob = "1994-01-01"
#     _dob = ""
#     def __init__(self, name, country, dob):
#         self.name = name
#         self.country = country
#         self.dob = dob
    
#     # instance method
#     # def calulate_age(self):
#     #     dob_obj = date.fromisoformat(self.dob)
#     #     return date.today().year - dob_obj.year
    
#     # class method
#     @classmethod
#     def calulate_age(cls, dob):
#         cls._dob
#         dob_obj = date.fromisoformat(dob)
#         return date.today().year - dob_obj.year
    
# danish = Person("dansh", "Pakistan", "1992-08-25")
# fahad = Person("fahad", "Pakistan", "1990-08-25")

# print(danish.name)
# print(danish.calulate_age(danish.dob))
# print(fahad.calulate_age(fahad.dob))

# Person.calulate_age(danish.dob)

# Person._dob

# local and global variable
# class syntax
# initialzing the class
# properties and methods
    # instance
    # class
# lifecycle of the object
# dunder/magic methods
# self
    

class MyClass:
    
    def __new__(cls):
         print("Creating instance")
         return super(MyClass, cls).__new__(cls)

    def __init__(self):
        print("Init is called")
        
    def __str__(self):
        return f"MyClass id:{self.id}"
    
    # destructor
    def __del__(self):
        print("deleting the object")
    

obj = MyClass()

obj.id = 100
print(obj)
obj = None
print("abcd")

    


"""
Write a Python program to create a calculator class. 
Include methods for basic arithmetic operations

Write a Python program to create a class representing a shopping cart. 
Include methods for adding and removing items, 
and calculating the total price.

Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements. - hard
Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements. - hard
Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements. - hard
Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes. - hard
"""