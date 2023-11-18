from models import notes_query

def assign_note_to_category(db, data):
    conn = db.connect()
    id = notes_query.assign_note_to_category(conn, data)
    db.disconnect(conn)
    return id