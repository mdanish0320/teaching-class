# display all the items of a list - example with string
cold_drinks = ["pepsi", "marinda", "7up", "sprit", "sting", "pakola", "coke"]

for cold_drink in cold_drinks:
    print(cold_drink)
    
# above loop will display
# pepsi
# marinda
# 7up
# sprit
# sting
# pakola
# coke


# display all the items of a list - example with integers
scores = [1001, 1, 55, -8, 0, 5, -7]

for score in scores:
    print(score)
# above loop will display
# 1001
# 1
# 55
# -8
# 0
# 5
# -7


# check if item exists in a list
wish = "coke"
cold_drinks = ["pepsi", "marinda", "7up", "sprit", "sting", "cocaloa", "coke"]

for cold_drink in cold_drinks:
    if cold_drink == wish:
        print("available")


# check if item exists in a list and also stop the loop if item found
wish = "xyz"
cold_drinks = ["pepsi", "marinda", "7up", "sprit", "sting", "cocaloa", "coke"]

for cold_drink in cold_drinks:
    if cold_drink == wish:
       print("available")
       break
     
     
# check if item exists in a list make sure the item "marinda" is reserved for other customer is not for sale
wish = "marinda"
cold_drinks = ["pepsi", "marinda", "7up", "sprit", "sting", "cocaloa", "coke"]

for cold_drink in cold_drinks:
    if cold_drink == 'marinda':
      continue
    
    if cold_drink == wish:
       print("available")
       break

# check if item exists in a list and also display "not available" if item doesn't exist
wish = "xyz"
cold_drinks = ["pepsi", "marinda", "7up", "sprit", "sting", "cocaloa", "coke"]

for cold_drink in cold_drinks:
    if cold_drink == wish:
       print("available")
       break
else:
    print("not avaiable")
