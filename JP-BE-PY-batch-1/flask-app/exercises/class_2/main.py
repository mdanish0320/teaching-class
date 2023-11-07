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
        log.warning("employee not found")
        return {
            "data": [],
            "message": "employee not found"
        }, 200

    return {
        "data": employees
    }, 200


@app.route("/employee/<user_id>", methods=['GET'])
def get_employee_profile(user_id):
    print("user_id", user_id)
    if user_id.isdigit() == False or int(user_id) <= 0:
        log.error("invalid ID")
        return {
            "error": {"message": "invalid id"}
        }, 400

    conn = db.mysqlconnect()
    employee = db.get_employee_by_id(conn, user_id)
    db.disconnect(conn)

    if employee is None:
        log.warning("employee not found")
        return {
            "error": {"message": "employee not found"}
        }, 400

    return {
        "data": employee
    }, 200


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
        return {
            "error": {"message": "API Accepts json data"}
        }, 400
    
    data = request.get_json()
    if (error := is_valid_employee_data(data)) is not None:
        return {
            "error": {"message": error}
        }, 400
    
    conn = db.mysqlconnect()
    employee_id = db.add_new_employee(conn, data)
    db.disconnect(conn)

    log.info("new employee added")
    return {
        "data": {"id": employee_id}
    }, 200


app.run(
    debug=True,
    port=3000
)
