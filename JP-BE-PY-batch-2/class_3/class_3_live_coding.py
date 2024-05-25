# install vs code extension
# python installation link and video

# arithmatic operator
# exponention

# 2 ^ 2 # 2 * 2
# 2 ^ 3 # 2 * 2 * 2
# 2 ^ 4 # 

# 2 ** 2 # 2 ^ 2 OR 2 * 2

# 2 ** 3 # 2 * 2 * 2 # 2 ^ 3


# modulus %

# even / odd
# cyclic rotation
# x  = "18523"

# print(10 % 2)
# # 10 - 2 = 8
# # 8 - 2 = 6
# # 2 - 2 = 0

# print(5 % 2)
# # 5 - 2 = 3
# # 3 - 2 = 1


# cyclic rotation
# print("0 % 3 = ", (0 % 3)) 
# print("1 % 3 = ", (1 % 3)) 
# print("2 % 3 = ", (2 % 3)) 
# print("3 % 3 = ", (3 % 3)) 
# print("4 % 3 = ", (4 % 3)) 
# print("5 % 3 = ", (5 % 3)) 
# print("6 % 3 = ", (6 % 3)) 
# print("7 % 3 = ", (7 % 3)) 

# find the last digit

# x = 106
# print(x % 10)


# 106 - 10 = 96
# 96 - 10 = 86
# .
# . 
# 16 - 10 = 6
# 6 - 10 = -4

# assignment operator
# x = 100

# # x = x + 50
# x += 50

# print(x)


# x = "100"

# # x = x + 50
# x += 50

# print(x)

# x = 100
# y = 50
# print(x + y)

# x = x + 50
# x += 50

# comparison operators

# ==
# !=
# >
# <
# >=

# x = 100
# y = 50

# print(x == y)


# x = 100
# y = 100

# print(x == y)



# x = "100"
# y = 100

# print(x == y)


# x = "100"
# y = "100"

# print(x == y)

# print(True == True)
# print(True == False)

# x = 100
# y = 100
# print(x == y) # true

# x = 100
# y = 1
# print(x != y) # true


# x = 100
# y = 1
# print(x < y) # true


# x = 100
# y = 100

# print(x == y)
# print(x >= y)
# print(x <= y)


# or , and

# x = 100
# y = 5
# z = 1000

# print( x > y and x > z) # False
# print( x > y and x < z) # True

# print( x > y or x > z) # 
# print( x > y or x < z) # 
# print( x < y or x > z) #

# confusion in precedence
# print(x > y and x > z or y < x) # True, False, True



# print((x > y and x > z) or y < x) # False, True

# print(x < y and (x > z or y < x)) # False and True


# # class task
# a=True
# b=True
# c=False
# d=False

# print(a and b) # 
# print(a or b)
# print(a or c)
# print(a and d)
# print(a and b or c)
# print(a or b and c)



# if statement syntax 
# print('sart') # out of if scope

# if condition: # which should evaluate to True/False. Only work with comparison operators
#     print("true") # if body
    
# print("end") # out of if scope

# x = 100
# y = 500
# if x < 100:
#     print("x is greater than y")
    
    
# Write a program to check the number is positive.
# Write a program to check the number is positive. User input.

# x = 100
# y = 500
# if x < 100:
#     print("x is greater than y")
# else:
#     print("x is less than y")

# Write a program to check whether a person is eligible to vote or not?
# Write a program to check whether a person is eligible to vote or not? User input

# Write a program to check whether a number is odd or even?
# hint: use modulus operator

# x = 101

# if x % 2 == 0:
#     print("even")
# else:
#     print("odd")

# elif example

# subject_math_score = 50
# if subject_math_score >= 80:
#     print("A+")
# elif subject_math_score >= 70:
#     print("A")
# else:
#     print("no grading")
    
# vowel chars are
# 1. a
# 2. e
# 3. i
# 4. o
# 5. u
# Write a program to check char is vowel or not. - elif

# char = input("enter vowel")

# if char == "a":
#     print("vowel")
# elif char == "e":
#     print("vowel")
# else:
#     print("not vowel")


# bank transaction
balance = 0
affiliated_card = True # meezan
is_senior_citizen = True
is_govt_employee = True
high_grade = True


print("initital balance", balance)

withdraw_amount = 50

if balance < withdraw_amount:
    print("insufficient balance")
    
deposit_amount = 500

# balance = balance + deposit_amount
balance += deposit_amount

print("after first depost:", balance)

withdraw_amount = 50
if withdraw_amount <= balance and (affiliated_card == True or is_senior_citizen):
    balance = balance - withdraw_amount
    print("after withdraw:", balance)
elif is_govt_employee and withdraw_amount <= balance:
    if high_grade:
        balance = balance - withdraw_amount
        print("after withdraw:", balance)
    elif is_govt_employee and withdraw_amount <= balance + 50:
       balance -= deposit_amount + 50
        