import logging
logging.basicConfig(level=logging.DEBUG)

# third party imports
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# local imports
from controller.employee import get_employee as GetEmployee

from db import mysql as mysql_db
employee_bp = Blueprint("profile_employee_service", __name__)
log = logging.getLogger("flask-app")

@employee_bp.route("/employee/<user_id>", methods=['GET'])
@jwt_required()
def get_employee_profile(user_id):
    if user_id.isdigit() == False or int(user_id) <= 0:
        log.error("invalid ID")
        return {
            "error": {"message": "invalid id"}
        }, 400
    
    current_user = get_jwt_identity()
    print("current_user", current_user)
    employee = GetEmployee.get_employee_profile(mysql_db, user_id)

    if len(employee) == 0:
        return {
            "error": {"message": "employee not found"}
        }, 400
    
    return {
        "data": employee
    }, 200