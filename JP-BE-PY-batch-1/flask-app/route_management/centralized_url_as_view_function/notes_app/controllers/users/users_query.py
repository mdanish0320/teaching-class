def add_new_user(db_conn, data):
    query = f"""
            INSERT INTO google_notes.user (name, email, password) 
            VALUES (%(name)s, %(email)s, %(password)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "name": data.get("name"),
            "email": data.get("email"),
            "password": data.get("password"),
        }
    )
    db_conn.commit()
    return cur.lastrowid

def login_user(db_conn, data):
    query = f"""
            SELECT id FROM user WHERE email=(%(email)s) AND password=(%(password)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "email": data.get("email"),
            "password": data.get("password")
        }
    )
    return cur.fetchone()