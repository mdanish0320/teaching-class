from db import db
from flask import request, Blueprint
from routes.users import utils
from services import token_services
from controllers.users import login_user as LoginUser

user_bp = Blueprint("login-user", "user_service")

@user_bp.route("/login", methods=["POST"])
def login_user():
    if not request.is_json:
        return {
            "error": {
                "message": "API accepts json data"
            }
        }, 400
    data = request.get_json()
    if (error := utils.validate_login_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    user_id = LoginUser.login_user(db, data)
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