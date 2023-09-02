l = [1, 2, 3, 4, 2, 3]  # this is a list
t = (1, 2, 3, 4, 2, 3)  # this is a tuple
s = {1, 2, 3, 4, 2, 3}  # this is a set

memory_location_of_list = id(l)
memory_location_of_tuple = id(t)
memory_location_of_set = id(s)

print(
    "memory location of list:", memory_location_of_list
)
print(
    "memory location of tuple:", memory_location_of_tuple
)
print(
    "memory location of set:", memory_location_of_set
)

# change state of the list, tuple and set
l.append(5)
l.append(6)
s.add(5)
s.add(6)
t += (5, 6)


# check the memory location again
# if memory location is changed then the data type is said to be immutable
# if memory location remains the same then the data type is said to be mutable
print("")

print(
    "memory location of list:", memory_location_of_list
)
print(
    "memory location of tuple:", memory_location_of_tuple
)
print(
    "memory location of set:", memory_location_of_set
)

print("")


print(
  "list:", memory_location_of_list == id(l)
)
print(
    "tuple:",memory_location_of_tuple == id(t)
)
print(
   "set:",memory_location_of_set == id(s)
)


# list down mutablitiy of data types

# str -> immutable
# int -> immutable
# boolean -> immutable
# tuple -> immutable

# list -> mutable
# dict -> mutable
# set -> mutable
