from models import notes_query

def get_user_category_notes(db, user_id, cat_id):
    conn = db.connect()
    notes = notes_query.get_user_category_notes(conn, user_id, cat_id)
    db.disconnect(conn)
    return notes