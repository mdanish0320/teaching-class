import random
import string
import requests


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


# add new employee
def login():
  url = "http://localhost:3000/login"

  r = requests.post(url, json={
    "username": "test", 
    "password": "test"
    }
  )
  response_data = r.json()
  print(response_data)
  return response_data['access_token']  

def protected_api(access_token):
  url = "http://localhost:3000/protected"
  r = requests.get(url, headers={
     "Authorization" : f"Bearer {access_token}"
  })
  response_data = r.json()
  print(response_data)


access_token = login()
protected_api(access_token)
