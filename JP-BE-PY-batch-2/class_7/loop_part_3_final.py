# loop using enumerate on list and dict
arr = [100, 200, 300, 400, 500]

# loop with range to display index and value of the list
for i in range(len(arr)):
    print(i, arr[i])

# using enumerate to display index and value
for i, val in enumerate(arr):
    print(i, val)
  
  
# class task
students = ["alice", "bob", "charlie"]
score = [80, 90, 100]

dictt = {
    "students": [],
    "score": []
}

for i, val in enumerate(students):
    dictt["students"].append(students[i])
    dictt["score"].append( score[i])
        

# while loop

# loop will run forever
while True:
    print("hello world")

# loop will run forver
x = 0
while x > 0 and x <= 10:
    print("hello world")

# loop wil run 10 times and break
x = 1
while x > 0 and x <= 10:
    x += 1
    print("hello world")

# loop will not run
x = 10
while False:
    print("hello world")

# what to change in the below code to make loop run 10 times only
# loop will run forever
x = 10
while x > 0:
    x += 1
    print("hello world")
    
    
# class task
# ask user input postive number and keep asking positive number and display   
# terminate the program when user input negative number 

# solution 1
user_number = int(input("enter positive number"))
while user_number > 0:
    print(user_number)
    user_number = int(input("enter positive number"))


# solution 2
while True:
    user_number = int(input("enter positive number"))    
    if user_number < 0:
        break
    print(user_number)
    


# nested loop
# find common number in given lists
list_1 = [10, 20, 30]
list_2 = [40, 50, 60, 30]

for item_1 in list_1:
    for item_2 in list_2:
        if item_1 == item_2:
            print("common number is", item_1)