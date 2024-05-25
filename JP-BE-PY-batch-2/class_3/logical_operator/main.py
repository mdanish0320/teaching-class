# Logical Operators
# Comparison between more than 2 operands
# below are the operators

# and -> it returns true if all the operands are true otherwise it returns false
# or  -> it returns true if any one of the operands are true and return false if all operands returns false 
# not -> it revers the value. if value is true it will make it false. if value is false, it will make it to true

print( True and True) # True
print( True or True)  # True
print( False and False)  # False
print( False or False)  # False
print( True and False)  # False
print( True or False)  # True


print((True and True) and (True and True))    # True
print((True and True) or (True and True))     # True

print((False and False) and (False and False)) # False
print((False or False) and (False or False))  # False

print((True and False) and (False and True))  # False
print((True or False) and (False or True))    # True

print((True and False) and (False or True))   # False
print((True and False) or (False or True))    # True


# confusion in precedence
# print(x > y and x > z or y < x) # True, False, True

# correct way of definding precedence
# print((x > y and x > z) or y < x) # False, True
# print(x < y and (x > z or y < x)) # False and True