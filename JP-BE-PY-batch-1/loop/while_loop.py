# while loop

x = 5
while x > 0:
    print(x)
    x -= 1 
    

# write a program to ask user number and the number must be between 1 and 10. 
# if other number is provided then ask user the number again
user_input = input("enter a number between 1 and 10 \n")
user_input = int(user_input)

while user_input < 0 or user_input > 10:
    user_input = input("please enter a number between 1 and 10 \n")
    user_input = int(user_input)

print("valid number is", user_input)
