from flask import Flask, request
import db
from query import get_employees_safe_query
import json

app = Flask(__name__)

@app.route("/employees", methods=['GET'])
def get_all_employees():
  params = request.args
  
  db_conn = db.mysqlconnect()

  employees = get_employees_safe_query(db_conn, params)
  
  if len(employees) == 0:
    employees = []
  
  return employees


app.run(debug=True, port=3000)