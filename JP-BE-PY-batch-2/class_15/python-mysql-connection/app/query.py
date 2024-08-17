def get_employees(db_conn):
  cur = db_conn.cursor()
  cur.execute("SELECT * FROM employees")
  return cur.fetchall()


def add_employee(db_conn, data):
  cur = db_conn.cursor()
  employee_id = data['employee_id']
  fname = data['fname']
  lname = data['lname']
  email = data['email']
  cur.execute(
    f"""
      INSERT INTO employees 
      VALUES (
        {employee_id}, 
        '{fname}',
        '{lname}', 
        '{email}', 
        '515.123.4567', 
        '1987-06-17', 
        'AD_PRES', 
        '24000.00', 
        '0.00', 
        '0', 
        '90'
      )

    """)
  db_conn.commit()
  
