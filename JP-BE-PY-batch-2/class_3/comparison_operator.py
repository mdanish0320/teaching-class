# comparison Operator
# below are the examples of comparison Operators
"""
Operator		Name					            Example	
==			    Equal					            x == y	
!=			    Not equal				          x != y	
>			      Greater than				      x > y	
<			      Less than				          x < y	
>=			    Greater than or equal to	x >= y	
<=			    Less than or equal to		  x <= y
"""

x = 5
y = 8
print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x < y:", x < y)    # True
print("x > y:", x > y)    # False
print("x <= y:", x <= y)  # True
print("x >= y:", x >= y)  # False


x = 10
y = 6
print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x < y:", x < y)    # False
print("x > y:", x > y)    # True
print("x <= y:", x <= y)  # False
print("x >= y:", x >= y)  # True

x = 20
y = 20
print("x == y:", x == y)  # True
print("x != y:", x != y)  # False
print("x < y:", x < y)    # False
print("x > y:", x > y)    # False
print("x <= y:", x <= y)  # True
print("x >= y:", x >= y)  # True



# live coding
x = 100
y = 50
print(x == y)


x = 100
y = 100
print(x == y)



x = "100"
y = 100
print(x == y)


x = "100"
y = "100"
print(x == y)


print(True == True)
print(True == False)

x = 100
y = 100
print(x == y) # true

x = 100
y = 1
print(x != y) # true


x = 100
y = 1
print(x < y) # true


x = 100
y = 100

print(x == y)
print(x >= y)
print(x <= y)
