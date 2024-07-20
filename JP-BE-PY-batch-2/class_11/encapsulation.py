class MyClass:
  def __init__(self):
    self.x = "x"
    self._x = "_x"
    self.__x = "__x_value"
    self.__salary = "_salary_value"
  
  def get_name(self):
    print(self.__x)
  
  # getter method
  @property
  def salary(self):
    return self.__salary
  
  # setter method
  @salary.setter
  def salary(self, amount):
    self.__salary = amount
    
x = MyClass()
print(x.x) # public property
print(x._x) # private property
# print(x.__x) # private property # error
print(x._MyClass__x) # name mangling

# using getther method
print(x.salary)