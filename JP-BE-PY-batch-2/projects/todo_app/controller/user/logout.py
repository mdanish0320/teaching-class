from flask import request, make_response

def logout():
  response = make_response("Logging out...")
  response.set_cookie('logged_in_user', '', expires=0)
  return response
  
  
  