import requests

# POST: data with content-type form-data
url = "http://localhost:3000/input/post/form-data"
r = requests.post(url, data={"name": "danish", "age": 30})
print(r)
print(r.content)

# POST: data with content-type urlencoded
url = "http://localhost:3000/input/post/form-urlencoded"
r = requests.post(url, data={"name": "danish", "age": 30})
print(r)
print(r.content)


# POST: data with content-type raw or json
url = "http://localhost:3000/input/post/json"
r = requests.post(url, json={"name": "danish", "age": 30})
print(r)
print(r.content)
print(r.json())
