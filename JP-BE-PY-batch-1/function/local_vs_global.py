counter = 0 # int is an immutable data type

print(
  "memory_location of var counter:",
  id(counter)
)

# to change value of the global variable, global keyword is required
def increment():
    global counter
    counter += 1

def decrement():
    global counter
    counter -= 1
    
# not need to add global variable to access the global variable
def display_counter_val():
  print(counter)

increment()
increment()
increment()
increment()
increment()

decrement()
decrement()

display_counter_val()  # it should display 3

print(
    "memory_location of var counter:",
    id(counter)
)
