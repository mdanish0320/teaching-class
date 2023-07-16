## Excercise
# Use input function and write a program that outputs below

# Hi USER_INPUT! Welcome back.


# Solution:

# method 1
name = input("Enter your name:\n")
print(f"Hi {name}! Welcome back.")

# method 2
name = input("Enter your name:\n")
print("Hi {}! Welcome back.".format(name))

# method 3
name = input("Enter your name:\n")
print("Hi %s! Welcome back." %(name))
