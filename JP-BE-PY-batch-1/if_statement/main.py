# if statement 
# it controls the flow of the program based on the condition provided
# review the below flow chart, this is how the if statement works
# https://i.ytimg.com/vi/WHH8Gx0u9Is/maxresdefault.jpg

# Syntax
condition = True
if condition == True:
  print("hello world")
else:
  print("hello universe")
# the above program will display "hello world"
  
condition = False
if condition == True:
  print("hello world")
else:
  print("hello universe")
# the above program will display "hello universe"

x = 20
if x == 5:
  print("the number is 5")
elif x == 10:
  print("the number is 10")
elif x == 15:
  print("the number is 15")
elif x == 20:
  print("the number is 20")
# the above program will display the number is 20


x = 25
if x == 5:
  print("the number is 5")
elif x == 10:
  print("the number is 10")
elif x == 15:
  print("the number is 15")
elif x == 20:
  print("the number is 20")
else:
  print("the number is not 5 or 10 or 15 or 20 :( ")
  # the above program will display "the number is not 5 or 10 or 15 or 20 :("
