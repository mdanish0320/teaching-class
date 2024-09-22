
def is_category_exists(db_conn, name, user_id):
    query = 'select * from categories where name=%s AND user_id=%s'
    
    cur = db_conn.cursor()
    cur.execute(query,(name, user_id,))
    return cur.fetchone() 
    
    
def create_category_query(db_conn, name, user_id):
    query = 'INSERT INTO categories (name, user_id) VALUES (%s, %s)'
    
    cur = db_conn.cursor()
    cur.execute(query, (name,user_id,)) 
    db_conn.commit()

def get_user_categories(db_conn, user_id, data):
    query = 'select * from categories WHERE 1=1 '

    condition = []
    if user_id is not None:
        query += " AND user_id=%s"
        condition.append(user_id)

    if data.get("name") is not None:
        query += " AND name=%s"
        condition.append(data.get("name"))

    
    cur = db_conn.cursor()
    cur.execute(query, tuple(condition))
    return cur.fetchall() 


def get_user_category(db_conn, id, user_id):
    query = 'select * from categories where id=%s AND user_id=%s'
    
    cur = db_conn.cursor()
    cur.execute(query,(id, user_id,))
    return cur.fetchone() 
    