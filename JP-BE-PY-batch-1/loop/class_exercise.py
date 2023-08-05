# check how many times loop iterating on a loop by using "hello world"
# by looking at the code please image the order of the print statement
wish = "7up"
cold_drinks = ["pepsi", "marinda", "7up", "sprit", "sting", "cocaloa", "coke"]

for cold_drink in cold_drinks:
    if cold_drink == wish:
       print("available")

    print("hello world")


# check how many times loop iterating on a loop by using "hello world"
# by addign the break statement what do you think now in what order the print statement get called
wish = "7up"
cold_drinks = ["pepsi", "marinda", "7up", "sprit", "sting", "cocaloa", "coke"]

for cold_drink in cold_drinks:
    if cold_drink == wish:
       print("available")
       break

    print("hello world")


# check how many times loop iterating on a loop by using "hello world"
# by addign the continue statement what do you think now in what order the print statement get called
wish = "7up"
cold_drinks = ["pepsi", "marinda", "7up", "sprit", "sting", "cocaloa", "coke"]

for cold_drink in cold_drinks:
    if cold_drink == wish:
       print("available")
       continue

    print("hello world")
