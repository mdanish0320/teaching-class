# add item in the end of the list
l = ["pizza", "burger", "sandwich", "bbq"]
l.append("anda-paratha")
print(l) # ["pizza", "burger", "sandwich", "bbq", "anda-paratha"]
l.append("chicken-roll")
print(l) # ["pizza", "burger", "sandwich", "bbq", "anda-paratha", "chicken-roll"]

# add item at specified index in the list
l = ["pizza", "burger", "sandwich", "bbq"]
l.insert(1, "anda-paratha")
print(l) # ["pizza", "anda-paratha", "burger", "sandwich", "bbq"]

# remove item from the end of the list
l = ["pizza", "burger", "sandwich", "bbq"]
l.pop()
print(l) # ["pizza", "burger", "sandwich"]

# remove item from the list by providing index
l = ["pizza", "burger", "sandwich", "bbq"]
l.pop(2)
print(l) # ["pizza", "burger", "bbq"]

# remove item from the list by value
l = ["pizza", "burger", "sandwich", "bbq"]
l.remove("burger")
print(l) # ["pizza", "sandwich", "bbq"]

# remove all items from the list - 1
l = ["pizza", "burger", "sandwich", "bbq"]
l.clear()
print(l) # []

# remove all items from the list - 2
l = ["pizza", "burger", "sandwich", "bbq"]
l = []
print(l) # []

# merge 2 lists
l1 = ["pizza", "burger", "sandwich", "bbq"]
l2 = ["anda-paratah", "chicken-roll"]
l1.extend(l2)
print(l1) # ["pizza", "burger", "sandwich", "bbq", "anda-paratah", "chicken-roll"]

# sort items in the list in ascending order
l1 = ['d', 'b', 'a', 'c']
l1.sort() # ['a', 'b', 'c', 'd']
print(l1)

# sort items in the list in descending order
l1 = ['d', 'b', 'a', 'c']
l1.sort(reverse=True) # ['d', 'c', 'b', 'a']
print(l1)