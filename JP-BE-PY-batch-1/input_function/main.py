# input function
"""
Definitino: In Python, we use the input() function to take input from the user. 
            Whatever user enters as input, the input function converts it into a string. 
            If user enters an integer value, input() function converts it into a string.
"""

name = input(f"enter your name:")
age = input("enter your age:")

print("name:", name)
print("age:", age)

# display the data type of the var
print(type(name))  # <class 'str' >
print(type(age))  # <class 'str' >

# NOTE:
# user will enter number i.e 30 while entering the age. But the age variable will not display int as type. It will always display str
