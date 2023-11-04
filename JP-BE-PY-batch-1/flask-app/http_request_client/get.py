import requests

# GET API with query string
url = "http://localhost:3000/input/get/query_string"
r = requests.get(url, params={"name": "danish", "age": 30})
print(r)
print(r.content)


# GET API with path_parameter
user_id = 1000
url = "http://localhost:3000/input/get/path_parameter" +"/"+ str(user_id)
r = requests.get(url)
print(r)
print(r.content)
