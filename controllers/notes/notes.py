from services import token_services
from flask import request
from controllers.notes import notes_query
import db

def validate_note_data(data):
    error_msg = None
    if data.get("name") is None or len(data.get("name").strip()) == 0:
        error_msg = "name field is required"
    if data.get("description") is None or len(data.get("description").strip()) == 0:
        error_msg = "description field is required"
    return error_msg

def validate_note_category_data(data):
    error_msg = None
    if data.get("note_id") is None or len(data.get("note_id").strip()) == 0:
        error_msg = "note_id field is required"
    if data.get("category_id") is None or len(data.get("category_id").strip()) == 0:
        error_msg = "category_id field is required"
    return error_msg

@token_services.token_decrypt
def add_new_note(user_id):
    if not request.is_json:
        return {
            "error": {
                "message": "API accepts json data"
            }
        }, 400
    data = request.get_json()
    if (error := validate_note_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    data["user_id"] = user_id
    conn = db.mysqlconnect()
    user_id = notes_query.add_new_note(conn, data)
    db.disconnect(conn)
    return {
        "data": {"id": user_id}
    }, 200

@token_services.token_decrypt
def assign_note(user_id):
    if not request.is_json:
        return {
            "error": {
                "message": "API accepts json data"
            }
        }, 400
    data = request.get_json()
    if (error := validate_note_category_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    conn = db.mysqlconnect()
    notes_query.assign_note_to_category(conn, data)
    db.disconnect(conn)
    return {
        "data": {
            "message": "note is assigned to category"
        }
    }, 200

@token_services.token_decrypt
def get_user_notes(user_id):
    conn = db.mysqlconnect()
    notes = notes_query.get_user_notes(conn, user_id)
    db.disconnect(conn)
    return {
        "data": notes
    }

@token_services.token_decrypt
def get_category_notes(user_id, catid):
    conn = db.mysqlconnect()
    notes = notes_query.get_user_category_notes(conn, user_id, catid)
    db.disconnect(conn)
    return {
        "data": notes
    }