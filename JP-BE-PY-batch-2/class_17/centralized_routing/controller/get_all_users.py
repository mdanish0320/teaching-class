from flask import request
def get_all_users():
    return f"user with having first and last names: {request.args}"