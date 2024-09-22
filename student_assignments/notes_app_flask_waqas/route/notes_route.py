from controller.api_blueprint import notes_bp
from controller.notes import create_notes,get_user_notes,delete_user_notes,update_user_notes

notes_bp.add_url_rule('/notes',view_func=create_notes,methods=['POST'])
notes_bp.add_url_rule('/notes',view_func=get_user_notes,methods=['GET'])
notes_bp.add_url_rule('/notes/<id>',view_func=delete_user_notes,methods=['DELETE'])
notes_bp.add_url_rule('/notes/<id>',view_func=update_user_notes,methods=['PUT'])
