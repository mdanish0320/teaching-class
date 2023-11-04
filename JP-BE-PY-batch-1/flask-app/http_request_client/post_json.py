import requests

url = "http://localhost:3000//input/post/json"

r = requests.post(url, json={"name": "danish", "age": 30})
print(r)
print(r.content)
print(r.json())
