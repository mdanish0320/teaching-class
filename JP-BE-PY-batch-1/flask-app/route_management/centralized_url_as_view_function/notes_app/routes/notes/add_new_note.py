from services import token_services
from flask import request, Blueprint
from models import notes_query
from controllers.notes import add_new_note as AddNote
from db import db
from routes.notes import utils

note_bp = Blueprint("add-note", "note_services")


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
    if (error := utils.validate_note_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    data["user_id"] = user_id
    user_id = AddNote.add_new_note(db, data)
    return {
        "data": {"id": user_id}
    }, 200