# class method
# covering 2 use case to use class method
# 1. accessing private class variable
# 2. creating instance of the class

class Employee:  
    # private variable by name mangling
    __employees = 100
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        Employee.__employees += 1
    
    @classmethod
    def create_instace(cls):
        # read the file named employee
        # loop over each row
        # create instance of each employee
        # store emplyee object somewhere
        return Employee(
            "muhammad",
            "danish",
            100,
            30
        )

    @classmethod
    def get_total_employees(cls):
        return cls.__employees

# this will raise an error
# print(
#     Employee.__employees # AttributeError: type object 'Employee' has no attribute '__employees'
# )


print(
  Employee.get_total_employees()
)


########################################
### Class Method: Second Use Case ######
########################################
print("---------------------------------")
print("\nClass Method: Second Use Case\n")
print("---------------------------------")

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @classmethod
    def create_instace(cls):
        # sudo code
        # read the file named employee
        # loop over each row
          # create instance of each employee
          # store emplyee object somewhere
        return cls(
            "muhammad",
            "danish"
        )


emp_1 = Employee.create_instace()
print(
    emp_1.fname,
    emp_1.lname
)






    # # utility/helper function
    # @staticmethod
    # def calculate_years_of_service(joining_date):
    #     print("years of service", 5)

    # # utility/helper function
    # @staticmethod
    # def calculate_age(dob):
    #     pass
