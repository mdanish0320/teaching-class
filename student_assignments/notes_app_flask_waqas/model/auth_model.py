import bcrypt


def create_user(db_conn, username, email, password):
    query = 'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)'
    try:
        with db_conn.cursor() as cur:
            cur.execute(query, (username, email, password)) 
        db_conn.commit()
        print("User created successfully.")
    except Exception as e:
        db_conn.rollback() 
        print(f"An error occurred: {e}")


def is_email_registered(db_conn , email , username):
    query = 'select * from users where email=%s or username=%s'
    try: 
        cur = db_conn.cursor()
        cur.execute(query,(email,username))
        result = cur.fetchall() 
        return result if result else None
    except Exception as e:
       return f'an error occurred {e}'
   


def check_user(db_conn, username, password):
    query = 'SELECT password,id FROM users WHERE username=%s'
    
    try:
        with db_conn.cursor() as cur:
            cur.execute(query, (username,))
            result = cur.fetchone()
            # print('result user',result['password'])
            if result:
                stored_password_hash = result['password']
                if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                    return result['id'] 
                else:
                    return False 
            else:
                return None 
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  
