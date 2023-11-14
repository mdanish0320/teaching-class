import logging
logging.basicConfig(level=logging.DEBUG)

# third party imports
from flask import Blueprint, request

# local imports
from controller.employee import list_employee as ListEmployee
from controller.employee import add_employee as AddEmployee
from controller.employee import get_employee as GetEmployee
from db import mysql as mysql_db
employee_bp = Blueprint("employee", "list_employee_service")
log = logging.getLogger("flask-app")
from model import employee as EmployeeModel


@employee_bp.route("/employee", methods=['GET'])
def get_employees_list():
    employees = ListEmployee.get_employee_list(mysql_db)
    if len(employees) == 0:
        return {
            "data": [],
            "message": "employee not found"
        }, 200
    
    return {
        "data": employees
    }, 200


# @employee_bp.route("/employee/<user_id>", methods=['GET'])
# def get_employee_profile(user_id):
#     if user_id.isdigit() == False or int(user_id) <= 0:
#         log.error("invalid ID")
#         return {
#             "error": {"message": "invalid id"}
#         }, 400
    
#     employee = GetEmployee.get_employee_profile(mysql_db, user_id)

#     if len(employee) == 0:
#         return {
#             "error": {"message": "employee not found"}
#         }, 400
    
#     return {
#         "data": employee
#     }, 200