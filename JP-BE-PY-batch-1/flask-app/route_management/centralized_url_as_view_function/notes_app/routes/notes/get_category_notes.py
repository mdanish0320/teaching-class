from services import token_services
from flask import request, Blueprint
from db import db
from controllers.notes import get_category_notes as GetCategoryNotes

note_bp = Blueprint("get-category-note", "note_services")

@note_bp.route("/category-note/<catid>", methods=["GET"])
@token_services.token_decrypt
def get_category_notes(user_id, catid):
    notes = GetCategoryNotes.get_user_category_notes(db, user_id, catid)
    return {
        "data": notes
    }