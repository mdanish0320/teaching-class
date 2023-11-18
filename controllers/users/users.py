import db
from models import users_query
from flask import request, Blueprint
from services import token_services
from users_validation import *;

user_bp = Blueprint("user", "user_service")

@user_bp.route("/user", methods=["POST"])
def add_new_user():
    if not request.is_json:
        return {
            "error": {
                "message": "API accepts json data"
            }
        }, 400
    data = request.get_json()
    if (error := validate_user_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    conn = db.mysqlconnect()
    user_id = users_query.add_new_user(conn, data)
    db.disconnect(conn)
    return {
        "data": {"id": user_id}
    }, 200

@user_bp.route("/login", methods=["POST"])
def login_user():
    if not request.is_json:
        return {
            "error": {
                "message": "API accepts json data"
            }
        }, 400
    data = request.get_json()
    if (error := validate_login_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    conn = db.mysqlconnect()
    user_id = users_query.login_user(conn, data)
    db.disconnect(conn)
    if (user_id != None):
        return {
            "message": "user login successfully",
            "token": token_services.enrypt(user_id["id"])
        }, 200
    else:
        return {
            "error": {
                "message": "invalid email or password"
            }
        }, 400