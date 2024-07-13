from datetime import date
class Person:
    # dob = "1994-01-01"
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    # instance method
    # def calulate_age(self):
    #     dob_obj = date.fromisoformat(self.dob)
    #     return date.today().year - dob_obj.year
    
    # class method
    @classmethod
    def calulate_age(cls, dob):
        dob_obj = date.fromisoformat(dob)
        return date.today().year - dob_obj.year