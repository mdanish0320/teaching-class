import logging
logging.basicConfig(level=logging.DEBUG)
import json

log = logging.getLogger("flask-app")
from model import employee as EmployeeModel

def get_employee_list(db):
    log.info("get all employees")

    conn = db.mysqlconnect()
    employees = EmployeeModel.get_all_employees(conn)
    db.disconnect(conn)
    
    if len(employees) == 0:
        log.warning("employee not found")
        employees = []
    
    return employees
