# display the number 0 to 9 using loop
for i in range(10):
  print(i)
  
  
# display the number 5 to 9 using loop
for i in range(5, 10):
  print(i)
  
  
# display the number 0 to 9 but incremented twice using loop
for i in range(5, 10, 2):
  print(i)
  

# reverse loop
# display the number 0 to -9 using loop
for i in range(0, -10, -1):
    print(i)



# display the multiple of table 2
for i in range(1, 11, 1):
    print(i * 2)


# check if item exists in a list. access the item using index
wish = "marinda"
cold_drinks = ["pepsi", "marinda", "7up", "sprit", "sting", "cocaloa", "coke"]

total_items_in_list = len(cold_drinks)
new_list =  list(range(total_items_in_list)) # [0, 1, 2, 3, 4, 5, 6]

for num in new_list:
   if cold_drinks[num] == wish:
        print("available")

