from services import token_services
from flask import request, Blueprint
from models import notes_query
from db import db
from routes.notes import utils
from controllers.notes import assign_note as AssignNote

note_bp = Blueprint("assign-note", "note_services")

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
    if (error := utils.validate_note_category_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    id = AssignNote.assign_note_to_category(db, data)
    return {
        "data": {
            "message": "note is assigned to category"
        }
    }, 200