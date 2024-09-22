

def create_notes_query(db_conn, title, content, cat_id,user_id):
    query = 'INSERT INTO notes (user_id,title,content,cat_id) VALUES (%s, %s, %s,%s)'
    try:
        with db_conn.cursor() as cur:
            cur.execute(query, (user_id,title, content, cat_id)) 
        db_conn.commit()
        print("note created successfully.")
    except Exception as e:
        db_conn.rollback() 
        print(f"An error occurred: {e}")


def is_user_exists(db_conn , id ):
    query = 'select id, email, username from users where id=%s'
    try: 
        cur = db_conn.cursor()
        cur.execute(query,(id,))
        result = cur.fetchall() 
        return result if result else None
    except Exception as e:
       return f'an error occurred {e}'


def is_category_exists(db_conn , id ):
    query = 'select * from categories where id=%s'
    try: 
        cur = db_conn.cursor()
        cur.execute(query,(id,))
        result = cur.fetchall() 
        return result if result else None
    except Exception as e:
       return f'an error occurred {e}'


def is_notes_exists(db_conn , id,uid ):
    query = 'select * from notes where id=%s and user_id=%s'
    try: 
        cur = db_conn.cursor()
        cur.execute(query,(id,uid))
        result = cur.fetchall() 
        return result if result else None
    except Exception as e:
        db_conn.rollback() 
        return f'an error occurred {e}'


def user_notes(db_conn , uid ):
    query = 'select * from notes where user_id=%s'
    try: 
        cur = db_conn.cursor()
        cur.execute(query,(uid,))
        result = cur.fetchall() 
        return result if result else None
    except Exception as e:
        db_conn.rollback() 
        return f'an error occurred {e}'


def delete_notes(db_conn , uid,id ):
    query = 'delete from notes where user_id=%s and id=%s'
    try: 
        cur = db_conn.cursor()
        cur.execute(query,(uid,id))
        db_conn.commit()
        print('deleted notes')
        # return result if result else None
    except Exception as e:
        db_conn.rollback() 
        
        return f'an error occurred {e}'


def update_notes(db_conn, uid, id, title=None, content=None, cat_id=None):
    query = 'UPDATE notes SET'
    fields = []
    
    if title is not None:
        query += ' title = %s'
        fields.append(title)
    
    if content is not None:
        query += ' content = %s'
        fields.append(content)
    
    if cat_id is not None:
        query += ' cat_id = %s'
        fields.append(int(cat_id))
    
    if title is None and content is None and cat_id is None:
        return "No fields to update"
    
    query += ' WHERE user_id = %s AND id = %s'
    fields.append(uid)
    fields.append(id)
    
    try:
        with db_conn.cursor() as cur:
            cur.execute(query, tuple(fields))
            db_conn.commit()

    except Exception as e:
        db_conn.rollback() 
        return f"An error occurred: {e}"
