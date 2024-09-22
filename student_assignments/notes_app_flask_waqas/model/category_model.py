
def is_category_created(db_conn,name):
    query = 'select * from categories where category_name=%s'
    try: 
        cur = db_conn.cursor()
        cur.execute(query,(name,))
        result = cur.fetchall() 
        return result if result else []
    except Exception as e:
       return f'an error occurred {e}'
    
def create_category_query(db_conn, name):
    query = 'INSERT INTO categories (category_name) VALUES (%s)'
    try:
        with db_conn.cursor() as cur:
            cur.execute(query, (name,)) 
        db_conn.commit()
        print("category created successfully.")
    except Exception as e:
        db_conn.rollback() 
        print(f"An error occurred: {e}")
    