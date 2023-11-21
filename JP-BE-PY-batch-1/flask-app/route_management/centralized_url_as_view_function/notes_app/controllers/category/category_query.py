def add_new_category(db_conn, data):
    query = f"""
            INSERT INTO google_notes.category (name) 
            VALUES (%(name)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "name": data.get("name")
        }
    )
    db_conn.commit()
    return cur.lastrowid

def get_all_categories(db_conn):
    query = f"""
            SELECT * FROM category 
            """
    cur = db_conn.cursor()
    cur.execute(
        query
    )
    return cur.fetchall()