from flask import request
import json

from model import db
from model.query import get_user_all_tasks

def get_all_tasks():
  user_id = request.cookies.get('logged_in_user')
  print("user_id", user_id)
  if user_id is None:
      return "please login"
  
  conn = db.mysqlconnect()
  tasks = get_user_all_tasks(conn, user_id)
  db.disconnect(conn)
  
  return json.dumps(tasks)
  