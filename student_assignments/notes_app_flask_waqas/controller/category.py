from flask import request

from db import mysqlconnection,diconnect
from utils.helper import check_missing_fields
from model.notes_model import is_user_exists
from model.category_model import create_category_query,is_category_created

def create_category():
    if request.cookies.get('user_id') is None:
        return "Please login"
    if request.is_json:
        conn = mysqlconnection()
        body = request.get_json()
        fields =['name']
        name = body.get('name')
        user_id = request.cookies.get('user_id')
        user = is_user_exists(conn,user_id)
        missing_fields = check_missing_fields(fields,body)
        
        if missing_fields:
            return (f'required fields {','.join(missing_fields)}') 
        if user:
            category = is_category_created(conn,name)
            print(category)
            if len(category):
                print('cat')
                return 'this category already exists'
            
            create_category_query(conn,name)
            diconnect(conn)
            return 'category created successfully'
        else:
            return 'wrong user'
    else:
        return 'Name is required'    
            