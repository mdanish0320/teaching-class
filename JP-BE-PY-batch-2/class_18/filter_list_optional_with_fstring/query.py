# http://localhost:3000/employees?reports_to=1088&job_title=Sales Rep
# http://localhost:3000/employees?reports_to=1088&job_title=Sales Rep' OR '1=1
def get_employees_harmful_query(db_conn, params):
  reports_to = params.get('reports_to')
  job_title = params.get("job_title")
  cur = db_conn.cursor()
  
  query = "select * from employees where 1=1"
    
  if reports_to is not None:
    query += f" AND reportsTo={reports_to}"
    
    
  if job_title is not None:
    query += f" AND jobTitle='{job_title}'" 

  cur.execute(query)
  return cur.fetchall()