from models import notes_query

def get_user_notes(db, user_id):
    conn = db.connect()
    notes = notes_query.get_user_notes(conn, user_id)
    db.disconnect(conn)
    return notes