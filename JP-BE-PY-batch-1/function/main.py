# functions

def func_name():
    print("hello world")

func_name()



# pass info into the function
def func_name_with_input(name):
  print("hello", name)

func_name_with_input("danish")
other_name = "fahad"
func_name_with_input(other_name)


# pass info into the function with more than one info
# positional arguments
def func_name_with_multiple_input(day, name):
  print(f"hello and good {day}, {name}")


func_name_with_multiple_input("morning", "danish")
func_name_with_multiple_input("evening", "danish")
func_name_with_multiple_input("night", "danish")


# pass info into the function with more than one info
# keyword arguments
def func_name_with_multiple_input(day, name):
  print(f"hello and good {day}, {name}")


func_name_with_multiple_input(day="morning", name="danish")
func_name_with_multiple_input(day="evening", name="danish")
func_name_with_multiple_input(day="night", name="danish")


# pass info into the function with more than one info
# default value
def func_name_with_multiple_input_that_contains_default_value(day='morning', name='danish'):
  print(f"hello and good {day}, {name}")


func_name_with_multiple_input() # hello and good morning danish
func_name_with_multiple_input("evening")  # hello and good evening danish
func_name_with_multiple_input("night", "fahad")  # hello and good night fahad

# Mix positional and keyword argument
# Note: Positional arguments and parameters always come first, keyword parameters without defaults always come second, and keyword parameters with defaults always come last.



# return value from function
def func_that_retuns_some_value(x, y):
  return x + y

x = func_name_with_input(5, 5)
print(x) # 10
