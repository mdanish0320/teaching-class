from services import token_services
from flask import request, Blueprint
from controllers.notes import get_notes as GetNotes
from db import db

note_bp = Blueprint("get-note", "note_services")

@note_bp.route("/note", methods=["GET"])
@token_services.token_decrypt
def get_user_notes(user_id):
    notes = GetNotes.get_user_notes(db, user_id)
    return {
        "data": notes
    }