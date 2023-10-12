def get_employees(db_conn):
  cur = db_conn.cursor()
  cur.execute("SELECT * FROM employees")
  return cur.fetchall()
  

