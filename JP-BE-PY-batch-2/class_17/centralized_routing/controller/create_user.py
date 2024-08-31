from flask import request
def create_user():
    return f"created new user: {request.get_json()}"