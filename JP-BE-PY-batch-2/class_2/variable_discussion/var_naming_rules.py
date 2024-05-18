# rules
"""
A variable name must start with a letter or the underscore
A variable name can only contain alpha-numeric characters and underscores
A variable name cannot be any of the Python reserved keywords (https://www.w3schools.com/python/python_ref_keywords.asp)
varibles are case-sensitive
variale follow Snake Case ( other cases are Camel Case,  Pascal Case)
"""

## invalid variable names: they are (but not limited to) reserved words of python language
# global = 10
# class = 11
# break = "somthing"
# if = "somthing"
# for = "somthing"
# finally = "somthing"
# from = "somthing"


## invalid varible names
# 30_cars = 30 # invalid
# car-30 = 30 # invalid
# car_._30 = 30 # invalid

# valid varaiable name
car_30 = 30
my_30_cars = 30

# difference cases  while writing the variable
my_cars = 30  # snake case -> for python
myCars = 30  # camel case
MyCars = 30  # Pascal

# in python, we follow snake case

# variables are case-sensitive
# both are different variables
"x != X"