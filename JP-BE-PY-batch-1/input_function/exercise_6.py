## Excercise
# ask user 2 numbers and display SUM, MULTIPLICATION, DIVISION AND SUBTRACTION
# example:
# INPUT_1 = 5
# INPUT_2 = 5
# OUTPUT:
# SUM: 10
# MULTIPLICATION: 25
# DIVISION: 0
# SUBTRACTION: 0


# Solution:
num_1 = input("Enter first number :\n")
num_2 = input("Enter second number :\n")

num_1 = int(num_1)
num_2 = int(num_2)

print("SUM:", num_1 + num_2)
print("SUBTRACTION:", num_1 - num_2)
print("MULTIPLICATION:", num_1 * num_2)
print("DIVISION:", num_1 / num_2)

