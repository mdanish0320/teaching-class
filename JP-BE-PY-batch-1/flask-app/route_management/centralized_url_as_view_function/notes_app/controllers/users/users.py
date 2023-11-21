from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

import db
from controllers.users import users_query
from services import token_services

def validate_user_data(data):
    error_msg = None
    if data.get("name") is None or len(data.get("name").strip()) == 0:
        error_msg = "name field is required"
    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"
    if data.get("password") is None or len(data.get("password").strip()) == 0:
        error_msg = "password field is required"
    return error_msg

def validate_login_data(data):
    error_msg = None
    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"
    if data.get("password") is None or len(data.get("password").strip()) == 0:
        error_msg = "password field is required"
    return error_msg

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
    data['password'] = generate_password_hash(data['password'], method='pbkdf2:sha256:1000')
    user_id = users_query.add_new_user(conn, data)
    db.disconnect(conn)
    return {
        "data": {"id": user_id}
    }, 200

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
    user = users_query.login_user(conn, data)
    
    db.disconnect(conn)
    if (check_password_hash(user.get("password"), data['password'])):
        return {
            "message": "user login successfully",
            "token": token_services.enrypt(user["id"])
        }, 200
    else:
        return {
            "error": {
                "message": "invalid email or password"
            }
        }, 400