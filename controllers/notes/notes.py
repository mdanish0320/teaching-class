from services import token_services
from flask import request, Blueprint
from models import notes_query
import db
from controllers.notes.notes_validation import *

note_bp = Blueprint("note", "note_services")


@note_bp.route("/note", methods=["POST"])
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
    note_id = notes_query.add_new_note(conn, data)
    db.disconnect(conn)
    return {
        "data": {"id": note_id}
    }, 200

@note_bp.route("/assign-note", methods=["POST"])
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

@note_bp.route("/note", methods=["GET"])
@token_services.token_decrypt
def get_user_notes(user_id):
    conn = db.mysqlconnect()
    notes = notes_query.get_user_notes(conn, user_id)
    db.disconnect(conn)
    return {
        "data": notes
    }

@note_bp.route("/category-note/<catid>", methods=["GET"])
@token_services.token_decrypt
def get_category_notes(user_id, catid):
    conn = db.mysqlconnect()
    notes = notes_query.get_user_category_notes(conn, user_id, catid)
    db.disconnect(conn)
    return {
        "data": notes
    }