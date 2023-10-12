import db
from query import get_employees
import json

db_conn = db.mysqlconnect()

employees = get_employees(db_conn)
print(
  json.dumps(employees, default=str, indent=4)
)