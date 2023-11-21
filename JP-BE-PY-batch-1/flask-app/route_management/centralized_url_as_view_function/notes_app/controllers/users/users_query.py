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
            SELECT * FROM user WHERE email=%(email)s
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "email": data.get("email")
        }
    )
    return cur.fetchone()