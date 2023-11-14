import logging
logging.basicConfig(level=logging.DEBUG)
import json

log = logging.getLogger("flask-app")
from model import employee as EmployeeModel

def get_employee_profile(db, user_id):
    log.info("get employee profile")

    conn = db.mysqlconnect()
    employee = EmployeeModel.get_employee_by_id(conn, user_id)
    db.disconnect(conn)

    if employee is None:
        log.warning("employee not found")
        employee = {}

    return employee


