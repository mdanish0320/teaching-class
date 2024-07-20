class Employee:
    def __init__(self, fname, lname, gender, nic, dob, salary, joining_date):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.nic = nic
        self.dob = dob
        self.salary = salary
        self.joining_date = joining_date

    def get_salary(self):
        return self.salary
      
class Cook(Employee):
    pass

class Driver(Employee):
    def __init__(self, fname, lname, gender, nic, dob, salary, joining_date, dln):
       super().__init__(fname, lname, gender, nic, dob, salary, joining_date)
       self.driving_licence_number = dln
    
    
# Employee()
obj = Driver("muhammad", "danish", "male", "123", "1994", "100", "2020", "100000" )
print(obj.fname)

print(obj.get_salary())
        
# 
# class Cook(Driver):
#     pass