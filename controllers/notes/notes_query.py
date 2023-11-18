def add_new_note(db_conn, data):
    query = f"""
            INSERT INTO google_notes.note (name, description, user_id) 
            VALUES (%(name)s, %(description)s, %(user_id)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "name": data.get("name"),
            "description": data.get("description"),
            "user_id": data.get("user_id"),
        }
    )
    db_conn.commit()
    return cur.lastrowid

def assign_note_to_category(db_conn, data):
    query = f"""
            INSERT INTO google_notes.note_category (note_id, category_id) 
            VALUES (%(note_id)s, %(category_id)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "note_id": data.get("note_id"),
            "category_id": data.get("category_id"),
        }
    )
    db_conn.commit()
    return cur.lastrowid

def get_user_notes(db_conn, user_id):
    query = f"""
            SELECT * FROM note WHERE user_id=(%(user_id)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "user_id": user_id,
        }
    )
    return cur.fetchall()

def get_user_category_notes(db_conn, user_id, cat_id):
    query = f"""
            SELECT * FROM note n
JOIN note_category nc ON n.id = nc.note_id
WHERE n.user_id = {user_id} AND nc.category_id = {cat_id};
            """
    cur = db_conn.cursor()
    cur.execute(
        query
    )
    return cur.fetchall()