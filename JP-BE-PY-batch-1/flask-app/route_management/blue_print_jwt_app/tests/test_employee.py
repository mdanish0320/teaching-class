import pytest
import sys
import random
import string
from unittest.mock import patch, Mock
from functools import wraps
from flask_jwt_extended import create_access_token

def mock_decorator(func):
    @wraps(func)
    def _token_required(*args, **kwargs):
        print("mock decorator")
        return func(1, *args, **kwargs)

    return _token_required


sys.path.append(".")  # Adds higher directory to python modules path.

# from controller.employee import EmployeeView
from app import app



# def test_get_employee_profile_api():
#     with (
#          patch('flask_jwt_extended.view_decorators.verify_jwt_in_request', new=Mock()) as verify_jwt_in_request,
#         patch('routes.employee.profile_employee.get_jwt_identity', new=Mock()) as get_jwt_identity
#     ):
#         verify_jwt_in_request.return_value = None
#         get_jwt_identity.return_value = 100
#         response = app.test_client().get("/employee/2")
#         print(response.status_code)
#         print(response.data)
#         print(response.json)

def test_get_employee_profile_api_2():
    with app.test_request_context():
        access_token = create_access_token(identity=20)
    
    response = app.test_client().get("/employee/2", headers={"Authorization": "Bearer " + access_token})
    print(response.status_code)
    print(response.data)
    print(response.json)


