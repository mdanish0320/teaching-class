import random
import string
import requests


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


# add new employee
def add_new_employee():
  url = "http://localhost:3000/employee"

  r = requests.post(url, json={
    "fname": "muhammad", 
    "lname": "danish",
    "email": random_char(5)+"@gmail.com"
    }
  )
  response_data = r.json()
  print(response_data)
  return response_data['data']['id']
  
def get_employee_by_id(employee_id):
  url = "http://localhost:3000/employee" + "/" + str(employee_id)
  r = requests.get(url)
  response_data = r.json()
  print(response_data)
  

def get_all_employees():
  url = "http://localhost:3000/employee"
  r = requests.get(url)
  response_data = r.json()
  print(response_data)


employee_id = add_new_employee()
get_employee_by_id(employee_id)
get_all_employees()
