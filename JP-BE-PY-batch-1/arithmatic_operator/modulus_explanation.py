# modulus
# Definition: It produces a remainder for the integer division. 
#             Thus, the remainder is also always an integer number only. 
#             If there is no remainder obtained, then we get the remainder as zero (0).


# practical usage 1: see the pattern of circular repetition

print("5 % 1=", 1 % 5)  # 1
print("5 % 2=", 2 % 5)  # 2
print("5 % 3=", 3 % 5)  # 3
print("5 % 4=", 4 % 5)  # 4
print("5 % 5=", 5 % 5)  # 0

print("----")
print("----")
print("----")

print("5 % 6=", 6 % 5)  # 1
print("5 % 7=", 7 % 5)  # 2
print("5 % 8=", 8 % 5)  # 3
print("5 % 9=", 9 % 5)  # 4
print("5 % 10=", 10 % 5)  # 0

# practical usage 2: see the pattern of circular repetition
# find out the last digit of any number

num = 1008
last_digit = num % 10
print(last_digit) # 8


num = 1008887104
last_digit = num % 10 
print(last_digit) # 4

# findout even and odd number

num = 6
is_even = num % 2
print(is_even) # 0,  we will take answer 0 as True


num = 9
is_even = num % 2
print(is_even)  # 1, we will take answer 1 as False
