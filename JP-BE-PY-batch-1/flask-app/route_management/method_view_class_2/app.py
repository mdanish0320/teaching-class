import logging
logging.basicConfig(level=logging.DEBUG)

# third party import
from flask import Flask, abort, make_response, request
from flask.views import MethodView

# local imports
from db import mysql as mysql_db
from controller.employee import EmployeeView
from model import employee as EmployeeModel

# global configurations
app = Flask(__name__)
log = logging.getLogger("flask-app")



app.add_url_rule('/employee', view_func=EmployeeView.as_view('employee_list', request, mysql_db, EmployeeModel), methods=['GET'], defaults={'user_id': None})
app.add_url_rule('/employee/<user_id>', view_func=EmployeeView.as_view('employee_profile', request, mysql_db, EmployeeModel), methods=['GET'])
app.add_url_rule('/employee', view_func=EmployeeView.as_view('employee_create', request, mysql_db, EmployeeModel), methods=['POST'])

if __name__ == "__main__":

    app.run(
        debug=True,
        port=3000
    )
