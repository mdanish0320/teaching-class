# http://localhost:3000/employees?reports_to=1088&job_title=Sales Rep
# http://localhost:3000/employees?reports_to=1088&job_title=Sales Rep' OR '1=1
def get_employees_safe_query(db_conn, params):
    reports_to = params.get('reports_to')
    job_title = params.get("job_title")
    cur = db_conn.cursor()

    query = "SELECT * FROM employees WHERE 1=1"
    condition = []

    if reports_to:
        query += " AND reportsTo = %s"
        condition.append(reports_to)

    if job_title:
        query += " AND jobTitle = %s"
        condition.append(job_title)

    cur.execute(query, tuple(condition))
    return cur.fetchall()