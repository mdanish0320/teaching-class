# fetch key and value both of list in loop
l = [100, 200, 300, 400]
for x, y in enumerate(l):
    print(x, y)
    
# 0 100
# 1 200
# 2 300
# 3 400


# fetch key and value both of dict in loop
obj = {
  "id": 1, 
  "name": "danish",
  "gender": "male"
}
for x, y in obj.items():
    print(x, y)

# id 1
# name danish
# gender male
