import db
from query import get_employees, add_employee
import json

data = {}
data['employee_id'] = input("enter employee id:\n")
data['fname'] = input("enter first name:\n")
data['lname'] = input("enter last name:\n")
data['email'] = input("enter email:\n")

db_conn = db.mysqlconnect()


add_employee(db_conn, data)


employees = get_employees(db_conn)
print(
  json.dumps(employees, default=str, indent=4)
)

