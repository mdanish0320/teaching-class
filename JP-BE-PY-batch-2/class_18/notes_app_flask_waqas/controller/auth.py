from flask import request,make_response

from db import mysqlconnection,diconnect
from model.auth_model import create_user, is_email_registered, get_user
from utils.helper import is_valid_email
 

def signup():
    if not request.is_json:
        return 'email, password and username are required in json', 400
    
    body = request.get_json(silent=True) # ignore error
    
    # explain
    if body is None or not body:
        return 'body is required', 400
    
    """
    if not body
    not body: This checks if body evaluates to a falsy value. In Python, several values are considered falsy, including:

        None
        Empty sequences or collections, such as [], {}, '' (empty string)
        The number 0 or 0.0
        False
    """
    
    username = body.get('username')
    email = body.get('email')
    password = body.get('password')
    
    if username is None or email is None or password is None:
        return 'email, password and username are required', 400
    
    if type(username) is not str or type(email) is not str or type(password) is not str:
        return 'invalid email, password or username', 400

    if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
        return 'email, password and username must not be empty', 400
    
    # optional
    if email.find("@") == -1 or email.find(".") == -1:
        return 'invalid email - 1', 400
    
    if is_valid_email(email) == False:
        return "invalid email - 2", 400
    
    try:
        conn = mysqlconnection()
    except Exception as e:
        return "mysql connection error", 500

    try:
        is_user = is_email_registered(conn, email)
        
        if(is_user):
            return 'username or email already registered', 400
        
        create_user(conn, username, email, password)
        
        return f'user created with {username} {email} ', 200            
    except Exception as e:
        return e    
    finally:
        diconnect(conn)
      


def login():
    conn = mysqlconnection()
    
    # explain negative testing/condition
    if request.is_json == False:
        return 'username and password are required in json', 400
    
    body = request.get_json(silent=True)
        
    if body is None or not body:
        return 'username or password missing'
    

    """
    if not body
    not body: This checks if body evaluates to a falsy value. In Python, several values are considered falsy, including:

        None
        Empty sequences or collections, such as [], {}, '' (empty string)
        The number 0 or 0.0
        False
    """
    
    email = body.get('email')
    password = body.get('password')
    
    if email is None or password is None:
        return 'email, password and username are required', 400
    
    if type(email) is not str or type(password) is not str:
        return 'invalid email, password or username', 400

    if len(email.strip()) == 0 or len(password.strip()) == 0:
        return 'email, password and username must not be empty', 400
    
    if is_valid_email(email) == False:
        return "invalid email - 2", 400
    
    try:
        conn = mysqlconnection()
    except Exception as e:
        return "mysql connection error", 500
        
    try:
        user = get_user(conn, email)

        # explain
        if user is None or user['password'] != password:
            return "invalid user credentials", 400
        
        res = make_response('user logged in!')
        res.set_cookie(
            'user_id',
            str(user['id']),   
            httponly=True,  
            max_age=3600,       
            path='/',            
            samesite='Lax' 
        )
        return res
    
    except Exception as e:
        print("error", e)
        return "something went wrong", 500
    finally:
        diconnect(conn)
      


def logout():
    res = make_response("logout successful")
    res.set_cookie("user_id", "", expires=0, path="/")
    return res
