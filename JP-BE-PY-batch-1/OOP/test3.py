class EmployeeInfo:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def raise_salary(self, amount):
      self.salary += amount  
      
emp_1 = EmployeeInfo("m", "danish", 1000)
emp_2 = EmployeeInfo("m", "fahad", 2000)

emp_1.raise_salary(200)
print(emp_1.salary)




def add_employee(fname, lname, salary):
  return {"fname":fname, "lname":lname, "salary":salary}
  
def raise_salary(emp, amount):
  emp['salary'] += amount


empp_1 = add_employee("m", "danish", 1000)
empp_2 = add_employee("m", "fahad", 2000)

raise_salary(empp_1, 200)
print(empp_1)
