# static method
# used as utility or helper function

from datetime import date

class Employee:  # Pascal Case
    def __init__(self, fname, lname, dob, joining_date):
        self.fname = fname
        self.lname = lname
        
        self.date_of_birth = dob
        self.joining_date = joining_date
    
    # utility/helper function
    @staticmethod
    def calculate_years_of_service(joining_date):
        dt_obj = date.fromisoformat(joining_date)
        return date.today().year - dt_obj.year

    # utility/helper function
    @staticmethod
    def calculate_age(dob):
        dt_obj = date.fromisoformat(dob)
        return date.today().year - dt_obj.year
      

emp_1 = Employee(
    "Muhammad",
    "Danish",
    "1994-01-01",
    "2020-01-01",
)

print(
  "years of service:", Employee.calculate_years_of_service(emp_1.joining_date)
)

print(
    "age:", Employee.calculate_age(emp_1.date_of_birth)
)
