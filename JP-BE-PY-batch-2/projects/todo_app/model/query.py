def create_user(db_conn, username, password):
    cur = db_conn.cursor()
    cur.execute(
        """
        INSERT INTO users (username, password) 
        VALUES (%s, %s)
        """,
        (username, password)
    )
    db_conn.commit()
  
def login_user(db_conn, username, password):
    cur = db_conn.cursor()
    cur.execute(
        """
        SELECT * FROM users WHERE username=%s AND password=%s limit 1
        """,
        (username, password)
    )
    return cur.fetchone()
  
  
def get_user_all_tasks(db_conn, user_id):
    cur = db_conn.cursor()
    cur.execute(
        """
        SELECT * FROM tasks WHERE user_id=%s
        """,
        (user_id)
    )
    return cur.fetchall()
