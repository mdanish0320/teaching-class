## encapsulation
"""
Encapsulation helps in controlling access to an object's state,
protecting it from unintended modifications, and enforcing data integrity.
"""
class Employee: 
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        
        # private variable (double underscore) achieved by name mangling
        self.__salary = self.validate_salary(salary)

    # getter
    def get_salary(self):
        return self.__salary

    # setter
    def set_salary(self, salary):
        self.__salary = self.validate_salary(salary)
        
    def validate_salary(self, salary):
        if salary <= 0:
            raise Exception("Salary cannot be 0")
        else:
            return salary

emp_1 = Employee(
        "Muhammad",
        "Danish",
        1000
      )

# this will raise an error
# print(
#   emp_1.__salary # AttributeError: 'Employee' object has no attribute '__salary'
# )
 
print(
    emp_1.get_salary()
)
print(
    emp_1.__dict__
)


emp_1.set_salary(5000)


print(
    emp_1.get_salary()
)
print(
    emp_1.__dict__
)



#######################
### Pythonic Way ######
#######################
print("\nPythonic Way\n")

class Employee:  # Pascal Case
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        
        # private variable (single underscore) by python guidelines
        self._salary = self.validate_salary(salary)

    @property
    def salary(self):
        print("salary getter method invoked")
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        print("salary setter method invoked")
        self._salary = new_salary
        
    def validate_salary(self, salary):
        if salary <= 0:
            raise Exception("Salary cannot be 0")
        else:
            return salary


emp_1 = Employee(
    "Muhammad",
    "Danish",
    1000
)
          
print(
    emp_1.salary
)
print(
    emp_1.__dict__
)


emp_1.salary = 5000


print(
    emp_1.salary
)
print(
    emp_1.__dict__
)
