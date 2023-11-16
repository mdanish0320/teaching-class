import logging
logging.basicConfig(level=logging.DEBUG)

# third party imports
from flask import Blueprint, request

# local imports
from controller.employee import list_employee as ListEmployee
from controller.employee import add_employee as AddEmployee
from controller.employee import get_employee as GetEmployee
from db import mysql as mysql_db
employee_bp = Blueprint("add_employee_service", __name__)

log = logging.getLogger("flask-app")
from model import employee as EmployeeModel

def _is_valid_employee_data(data):
    error_msg = None

    if data.get("fname") is None or len(data.get("fname").strip()) == 0:
        error_msg = "fname field is required"

    if data.get("lname") is None or len(data.get("lname").strip()) == 0:
        error_msg = "lname field is required"

    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"

    return error_msg

@employee_bp.route("/employee", methods=['POST'])
def add_new_employee():
    if not request.is_json:
        return {
            "error": {"message": "API Accepts json data"}
        }, 400
    
    data = request.get_json()
    if (error := _is_valid_employee_data(data)) is not None:
        return {
            "error": {"message": error}
        }, 400
    
    employee_id = AddEmployee.add_new_employee(mysql_db, data)

    return {
        "data": {"id": employee_id}
    }, 200