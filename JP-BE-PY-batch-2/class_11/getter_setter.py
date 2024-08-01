class Employee:
    def __init__(self, name, birth_date):
        self.__name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

E =Employee("danish", "1994")

# reading example 
print(E.name) # correct 
print(E.name()) # wrong 
print(E.__name) # wrong 

# updating value example 
E.name = "Fahad"# correct

# Attribute ki trah treat krega