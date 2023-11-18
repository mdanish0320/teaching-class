from models import notes_query

def add_new_note(db, data):
    conn = db.connect()
    user_id = notes_query.add_new_note(conn, data)
    db.disconnect(conn)
    return user_id
