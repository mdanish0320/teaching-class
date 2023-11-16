import logging
logging.basicConfig(level=logging.DEBUG)

# third party imports
from flask import Blueprint, request
from flask_jwt_extended import create_access_token

# local imports
from db import mysql as mysql_db
user_bp = Blueprint("user_login", __name__)

log = logging.getLogger("flask-app")
from model import employee as EmployeeModel


@user_bp.route("/user/login", methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return {"msg": "Bad username or password"}, 401

    access_token = create_access_token(identity=username)
    return {'access_token':access_token}, 200
