from db import db
from controllers.users import add_new_user as AddNewUser
from flask import request, Blueprint
from routes.users import utils

user_bp = Blueprint("add-user", "user_service")

@user_bp.route("/user", methods=["POST"])
def add_new_user():
    if not request.is_json:
        return {
            "error": {
                "message": "API accepts json data"
            }
        }, 400
    data = request.get_json()
    if (error := utils.validate_user_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    user_id = AddNewUser.add_new_user(db, data)
    return {
        "data": {"id": user_id}
    }, 200