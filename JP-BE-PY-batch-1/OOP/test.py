class Employee:
    # Class-wide counter for the number of employees
    total_employees = 0
    
    @classmethod
    def stat(cls):
      return cls.total_employees
    
    @staticmethod
    def stat():
      return Employee.total_employees

print(
  Employee.total_employees
)

emp_1 = Employee()
print(
    emp_1.total_employees
)


Employee.total_employees = 10

print(
    Employee.total_employees
)

emp_2 = Employee()
print(
  emp_2.total_employees
)


emp_1 = Employee()
print(
    emp_1.total_employees
)
