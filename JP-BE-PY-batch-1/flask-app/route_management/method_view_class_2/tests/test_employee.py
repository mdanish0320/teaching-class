import pytest
import sys
import random
import string

sys.path.append(".")  # Adds higher directory to python modules path.
from controller.employee import EmployeeView
from app import app

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


# pytest -ssv
def test_list_employees():
    e = EmployeeView(
        {},
        {},
        {},
    )

    print(e.test_this_function())

def test_list_employee_api():
    response = app.test_client().get("/employee")
    print(response.status_code)
    print(response.json)
    print(response.data)

def test_search_in_list_employee_api():
    response = app.test_client().get("/employee", query_string={"name": "danish", "age": 30})
    # response = app.test_client().get("/employee", json={"abc": 20000})
    # response = app.test_client().get("/employee", data={"id": 12222})
    print(response.status_code)
    print(response.json)
    print(response.data)

def test_create_employee_api():
    response = app.test_client().post("/employee", json={
    "fname": "muhammad", 
    "lname": "danish",
    "email": random_char(5)+"@gmail.com"
    })
    print(response.status_code)
    print(response.data)
    print(response.json)


def test_get_employee_profile_api():
    response = app.test_client().get("/employee/1")
    print(response.status_code)
    print(response.data)
    print(response.json)


