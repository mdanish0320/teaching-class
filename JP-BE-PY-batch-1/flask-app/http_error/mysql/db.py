import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="", # empty password
        db='test_db_1',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("db connected")
    return conn

def disconnect(conn):
  conn.close()


def get_all_employees(db_conn):
   # fetch data from db
    query = "SELECT * FROM employee"
    cur = db_conn.cursor()
    cur.execute(query)
    
    return cur.fetchall()
    

def get_employee_by_id(db_conn, employee_id):
   # fetch data from db
    query = f"SELECT * FROM employee WHERE id=%(employee_id)s"
    cur = db_conn.cursor()
    cur.execute(query, {
        "employee_id": employee_id
    })
    
    return cur.fetchone()

def add_new_employee(db_conn, data):
    # add record into databse
    query = f"""
                INSERT INTO employee (fname, lname, email, manager_id, job_title) 
                VALUES (%(fname)s, %(lname)s, %(email)s, %(manager_id)s, %(job_title)s)
            """
    cur = db_conn.cursor()
    cur.execute(query, {
        "fname": data.get("fname"),
        "lname": data.get("lname"),
        "email": data.get("email"),
        "manager_id": data.get("manager_id", 0),
        "job_title": data.get("job_title"),
    })
    
    # save the changes permanently
    db_conn.commit()
    
    return cur.lastrowid
