import logging
logging.basicConfig(level=logging.DEBUG)
import json

log = logging.getLogger("flask-app")
from model import employee as EmployeeModel

def add_new_employee(
        db,
        input_data
):
    
    conn = db.mysqlconnect()
    employee_id = EmployeeModel.add_new_employee(conn, input_data)
    db.disconnect(conn)

    log.info("new employee added")
    
    return employee_id