# escape characters

"""
Definition: To insert characters that are illegal in a string, use an escape character. 
            An escape character is a backslash \ followed by the character you want to insert.
"""

name = "my name is danish"
age = "I'm 30"

#  \n  is used for adding new line
print(name + "\n" + age) # it will print name and age in new separate lines

#  \t  is used for adding 4 spaces
print(name + "\t" + age)  # it will print name and age with 4 spaces between them

# \' and \" used for adding quotation marks safetly
print('I\'m 30')
print("I\"m 30")


