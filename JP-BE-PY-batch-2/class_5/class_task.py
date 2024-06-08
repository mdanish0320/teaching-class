# create a list of juices, add 5 items using append
# creat a list of cars, add 3 items using insert
# remove last time from the list ["bed", "table", "chair", "sofa"] using pop and len

# remove the item "chair" from the list ["bed", "table", "chair", "sofa"] using del and remove
furniture = ["bed", "table", "chair", "sofa"]
furniture.remove("chair")
print(furniture)

furniture = ["bed", "table", "chair", "sofa"]
chair_index = furniture.index("chair")
del furniture[chair_index]