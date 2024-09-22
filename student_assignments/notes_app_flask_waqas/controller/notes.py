from flask import request

from db import mysqlconnection,diconnect
from model.notes_model import create_notes_query,is_user_exists,is_category_exists,user_notes,delete_notes,update_notes,is_notes_exists
from utils.helper import check_missing_fields

def create_notes():
    # checking user logged in or not 
    if request.cookies.get('user_id') is None:
        return "Please login"
    
    if request.is_json:
        conn = mysqlconnection()
        body = request.get_json()
        fields =['title','content']
        title = body.get('title')
        content = body.get('content')
        cat_id = body.get('cat_id')
        user_id = request.cookies.get('user_id')
        user = is_user_exists(conn,user_id)
        missing_fields = check_missing_fields(fields,body)
        
        if missing_fields:
            # print(missing_fields)
            return (f'required fields {','.join(missing_fields)}') 
        
        # if user exists 
        if user:
            # checking if category id not null
            if cat_id is not None:
                category = is_category_exists(conn,int(cat_id))
                
                if category is None:
                    return 'invalid category id'
                
                # it will run if category id is valid 
                create_notes_query(conn,title,content,cat_id,int(user_id))
                diconnect(conn)
                return 'note created '
            
            # it will run withoud category id 
            create_notes_query(conn,title,content,None,int(user_id))
            diconnect(conn)
            return 'note created'
        else:
            return 'user does not exists'
    else:
        return "Title and content are required!"
    
 
def get_user_notes():
    # checking user logged in or not 
    if request.cookies.get('user_id') is None:
        return "Please login"
    
    conn = mysqlconnection()
    user_id = request.cookies.get('user_id')  
    notes = user_notes(conn,int(user_id))
    print(notes)
    diconnect(conn)
    
    return{
        'data':notes,
        'msg':'notes fetched successfully!',
        "status":200
    }

def delete_user_notes(id):
    # checking user logged in or not 
    if request.cookies.get('user_id') is None:
        return "Please login"
    if id is None:
        return 'notes id is required'
    try:
        notes_id = int(id)
    except Exception as e:
        return 'invalid id'    
    conn = mysqlconnection()
    user_id = request.cookies.get('user_id')
    notes = is_notes_exists(conn,id,int(user_id))   
    if notes:   
        delete_notes(conn,int(user_id),notes_id)
     # print(notes)
        diconnect(conn)
    
        return{
        # 'data':notes,
        'msg':'notes deleted successfully!',
        "status":200
    }
    else:
        return 'Notes not found'
        
        
def update_user_notes(id):
    # checking user logged in or not 
    if request.cookies.get('user_id') is None:
        return "Please login"
    
    if id is None:
        return 'notes id is required'
    
    try:
        notes_id = int(id)
    except Exception as e:
        return 'invalid id'
    if request.is_json:
        body = request.get_json()
        title = body.get('title')    
        content = body.get('content')    
        cat_id = body.get('cat_id')    
        conn = mysqlconnection()
        user_id = request.cookies.get('user_id')
        notes = is_notes_exists(conn,id,int(user_id)) 
        # print(notes)
        if notes:
            update_notes(conn,int(user_id),notes_id,title,content,cat_id)
            diconnect(conn)
            return{
        'msg':'notes updated successfully!',
        "status":200
        }
        else:
            return 'notes not found'    
    else:
        return 'Please provide title or content'    
        