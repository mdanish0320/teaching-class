from services import token_services
from flask import request
from controllers.category import category_query
import db

def validate_category(data):
    error_msg = None
    if data.get("name") is None or len(data.get("name").strip()) == 0:
        error_msg = "name field is required"

    return error_msg

@token_services.token_decrypt
def add_category(user_id):
    if not request.is_json:
        return {
            "error": {
                "message": "API accepts json data"
            }
        }, 400
    data = request.get_json()
    if (error := validate_category(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    data["user_id"] = user_id
    conn = db.mysqlconnect()
    user_id = category_query.add_new_category(conn, data)
    db.disconnect(conn)
    return {
        "data": {"id": user_id}
    }, 200


@token_services.token_decrypt
def get_cagtegories(user_id):
    conn = db.mysqlconnect()
    categories = category_query.get_all_categories(conn)
    db.disconnect(conn)
    return {
        "data": categories
    }, 200

