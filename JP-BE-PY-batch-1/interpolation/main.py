# string interpolation
"""
Definition: string interpolation is the process of 
            evaluating a string literal containing one or more placeholders, 
            yielding a result in which the placeholders are replaced with their corresponding values
"""

# method: 1
name = "danish"
age = 30

print(f"My name is {name}. I'm {age}")
print(f"My name is {name}. I'm {age}")


# method: 2
name = "danish"
age = 30
print("My name is {}. I'm {}".format(name, age))


# method: 3
name = "danish"
age = 30
z = "My name is %s. I'm %s" %(name, age)
print(z)


# Here is the link that writes other way of string interpolation
# https://www.programiz.com/python-programming/string-interpolation

