import requests

url = "http://localhost:3000/input/post/form-data"

r = requests.post(url, data={"name": "danish", "age": 30})
print(r)
print(r.content)