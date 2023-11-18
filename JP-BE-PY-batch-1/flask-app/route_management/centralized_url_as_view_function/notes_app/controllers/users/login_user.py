from models import users_query

def login_user(db, data):
    conn = db.connect()
    user_id = users_query.login_user(conn, data)
    db.disconnect(conn)
    return user_id