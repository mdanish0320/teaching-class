from flask import request, make_response
from model import db
from model.query import login_user

def login():
  data = request.get_json()
  
  username = data.get("username")
  password = data.get("password")
  
  conn = db.mysqlconnect()
  user = login_user(conn, username, password)
  db.disconnect(conn)
  
  if user is None:
    return "user not found", 400
  
  response = make_response(user)
  response.set_cookie('logged_in_user', str(user['id']), path='/', httponly=True)

  
  return response
  
  
  