import requests

url = "http://localhost:3000/input/get/query_string"

r = requests.get(url, params={"name": "danish", "age": 30})
print(r)
print(r.content)