
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