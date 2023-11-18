from models import users_query

def add_new_user(db, data):
    conn = db.connect()
    user_id = users_query.add_new_user(conn, data)
    db.disconnect(conn)
    return user_id