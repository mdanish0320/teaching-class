def create_user(db_conn, username, email, password):
    query = 'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)'
    
    cur = db_conn.cursor()
    cur.execute(query, (username, email, password)) 
    db_conn.commit()


def is_email_registered(db_conn , email):
    query = 'select * from users where email=%s'
    
    cur = db_conn.cursor()
    cur.execute(query,(email))
    result = cur.fetchone() 
    return result if result else None
   


def get_user(db_conn, email):
    query = 'SELECT * FROM users WHERE email=%s'

    cur = db_conn.cursor()
    cur.execute(query, (email,))
    return cur.fetchone()

def is_user_exists(db_conn , id):
    query = 'select count(*) from users where id=%s'
    
    cur = db_conn.cursor()
    cur.execute(query,(id,))
    result = cur.fetchone() 
    return result if result else None
    
