from flask import request
from model import db
from model.query import create_user

def signup():
  data = request.get_json() 
  
  conn = db.mysqlconnect()
  
  username = data.get("username")
  password = data.get("password")
  try:
    create_user(conn, username, password)
  except Exception as e:
    print("error:", e)
    return "error while creating user", 400
  
  db.disconnect(conn)
  return "user created"
  
  