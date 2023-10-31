import logging
logging.basicConfig(level=logging.DEBUG)
import json


from flask import Flask, abort, make_response, request

from mysql import db

app = Flask(__name__)
log = logging.getLogger("flask-app")


@app.route("/employee", methods=['GET'])
def get_employees():
    log.info("get all employees")

    conn = db.mysqlconnect()
    employees = db.get_all_employees(conn)
    db.disconnect(conn)
    
    if len(employees) == 0:
        log.warning("no data found")
        return make_response("no data found", 200)

    return employees


@app.route("/employee/<id>", methods=['GET'])
def get_employee_profile(id):
    
    if int(id) <= 0:
        log.error("invalid ID")
        return make_response("Invalid ID", 400)

    conn = db.mysqlconnect()
    employee = db.get_employee_by_id(conn, id)
    db.disconnect(conn)

    if employee is None:
        log.warning("no data found")
        return make_response(
            "Employee not found", 200
        )

    return employee


def is_valid_employee_data(data):
    error_msg = None

    if data.get("fname") is None or len(data.get("fname").strip()) == 0:
        error_msg = "fname field is required"

    if data.get("lname") is None or len(data.get("lname").strip()) == 0:
        error_msg = "lname field is required"

    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"

    return error_msg

@app.route("/employee", methods=['POST'])
def add_new_employee():
    if not request.is_json:
        return make_response("API accepts json data", 400)
    
    data = request.get_json()
    if (error := is_valid_employee_data(data)) is not None:
        return make_response(error, 400)
    
    conn = db.mysqlconnect()
    employee = db.add_new_employee(conn, data)
    db.disconnect(conn)

    return "success"


app.run(
    debug=True,
    port=3000
)