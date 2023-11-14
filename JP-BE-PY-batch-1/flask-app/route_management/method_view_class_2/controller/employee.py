import logging
logging.basicConfig(level=logging.DEBUG)
import json

from flask.views import MethodView

from helper.common import token_required

log = logging.getLogger("flask-app")

class EmployeeView(MethodView):
    def __init__(self, request, db, model):
        self.request = request
        self.db = db
        self.model = model

    @token_required
    def test_this_function(self, data):
        print(self.request)
        print(data)
        return 123

    def _get_employee_list(self):
        log.info("get all employees")

        conn = self.db.mysqlconnect()
        employees = self.model.get_all_employees(conn)
        self.db.disconnect(conn)
        
        if len(employees) == 0:
            log.warning("employee not found")
            return {
                "data": [],
                "message": "employee not found"
            }, 200

        return {
            "data": employees
        }, 200
    
    def _get_employee_profile(self, user_id):
        log.info("get employee profile")

        if user_id.isdigit() == False or int(user_id) <= 0:
            log.error("invalid ID")
            return {
                "error": {"message": "invalid id"}
            }, 400

        conn = self.db.mysqlconnect()
        employee = self.model.get_employee_by_id(conn, user_id)
        self.db.disconnect(conn)

        if employee is None:
            log.warning("employee not found")
            return {
                "error": {"message": "employee not found"}
            }, 400

        return {
            "data": employee
        }, 200

    def _is_valid_employee_data(self, data):
        error_msg = None

        if data.get("fname") is None or len(data.get("fname").strip()) == 0:
            error_msg = "fname field is required"

        if data.get("lname") is None or len(data.get("lname").strip()) == 0:
            error_msg = "lname field is required"

        if data.get("email") is None or len(data.get("email").strip()) == 0:
            error_msg = "email field is required"

        return error_msg
    
    def get(self, user_id):
        if user_id is None:
            return self._get_employee_list()
        else:
            return self._get_employee_profile(user_id)

    def post(self):
        
        if not self.request.is_json:
            return {
                "error": {"message": "API Accepts json data"}
            }, 400
        
        data = self.request.get_json()
        if (error := self._is_valid_employee_data(data)) is not None:
            return {
                "error": {"message": error}
            }, 400
        
        conn = self.db.mysqlconnect()
        employee_id = self.model.add_new_employee(conn, data)
        self.db.disconnect(conn)

        log.info("new employee added")
        return {
            "data": {"id": employee_id}
        }, 200