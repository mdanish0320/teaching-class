from flask import request,make_response

from db import mysqlconnection,diconnect
from model.auth_model import create_user,is_email_registered,check_user
from utils.helper import hash_password,check_missing_fields
 

def signup():
    conn = mysqlconnection()
    fields =['username','email','password']
    if request.is_json:
        body = request.get_json(silent=True)
        # print('hello',body)
        if body is None or not body:
           return 'body is required'
        username = body.get('username')
        email = body.get('email')
        password = body.get('password')
        missing_fields = check_missing_fields(fields,body)
        if missing_fields:
            # print(missing_fields)
            return (f'required fields {','.join(missing_fields)}') 
           
        else:
            try:
                is_user = is_email_registered(conn,email,username)
                # print('is user',is_user)
                if(is_user):
                    return 'username or email already registered'
                
                hash = hash_password(password)
                user_create = create_user(conn,username,email,hash)
                # print(user_create)
                diconnect(conn)
                return f'user created with {username} {email} '            
            except Exception as e:
                return e    
    else:
      return 'email, password and username are required'


# login endpoint function 
def login():
    conn = mysqlconnection()
    fields =['username','password']
    if request.is_json:
        body = request.get_json(silent=True)
        # print('hello',body)
        if body is None or not body:
           return 'username or password missing'
        username = body.get('username')
        password = body.get('password')
        missing_fields = check_missing_fields(fields,body)
        
        if missing_fields:
            return (f'required fields {','.join(missing_fields)}') 
           
        else:
            try:
                is_user = check_user(conn,username,password)
                # print('is user',is_user)
                if(is_user):
                    print('user found')
                    # diconnect(conn)
                    res = make_response('user logged in!')
                    res.set_cookie(
                        'user_id',
                        str(is_user),   
                        httponly=True,  
                        max_age=3600,       
                        path='/',            
                        samesite='Lax' 
                    )
                    return res
                
                else :
                    res = make_response("user not found")
                    res.set_cookie("user_id", "", expires=0, path="/")
                    return res           
            except Exception as e:
                return e    
    else:
      return 'username and password are required'


def logout_user():
    res = make_response("logout successful")
    res.set_cookie("user_id", "", expires=0, path="/")
    return res
