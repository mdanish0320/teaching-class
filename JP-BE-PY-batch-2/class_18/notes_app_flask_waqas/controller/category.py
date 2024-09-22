from flask import request

from db import mysqlconnection, diconnect
from model.auth_model import is_user_exists
from model.category_model import create_category_query, is_category_exists, get_user_categories, get_user_category

def create_category():
    # check if user logged in
    if request.cookies.get('user_id') is None:
        return "Please login", 401
    
    if not request.is_json:
        return 'name is required in json', 400
    
    user_id = request.cookies.get('user_id')
    body = request.get_json()
    name = body.get('name')
    
    conn = mysqlconnection()
    
    user = is_user_exists(conn, user_id)
    
    if user is None:
        return "user not found", 400
    
    category = is_category_exists(conn, name, user_id)
    
    if category is not None:
        return f"category '{name}' already exists", 400
    
    create_category_query(conn, name, user_id)

    diconnect(conn)
    
    return 'category created successfully'


def get_categories():
    # check if user logged in
    if request.cookies.get('user_id') is None:
        return "Please login", 401
    
    user_id = request.cookies.get('user_id')
    input_data = request.args
    
    conn = mysqlconnection()

    
    categories = get_user_categories(conn, user_id, input_data)
    
    if len(categories) == 0:
        categories = []

    diconnect(conn)
    
    return categories, 200


def get_category(id):
    # check if user logged in
    if request.cookies.get('user_id') is None:
        return "Please login", 401
    
    user_id = request.cookies.get('user_id')
    
    conn = mysqlconnection()

    
    category = get_user_category(conn, id, user_id)

    if category is None:
        category = {}

    diconnect(conn)
    
    return category, 200
            