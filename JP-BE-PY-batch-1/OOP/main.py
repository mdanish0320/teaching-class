# 3 important things

# 1. properties
    # only instance variable
# 2. behavour
    # only instance method
# 3. constructor/desctructor

# 2 ways to call instance method
# obj = MyClass()
# obj.my_method()
# and
# MyClass.my_method(obj)

# there is no big difference in both as per our examples
### create program to display the difference between procedural and OOP
### force on 3 points
### 1. code readablility
### 2. code complexity
### 3. state management: global state vs individutal object state

# write a program in procedural way
# tell students to covert the logic in OOP

# instance variable vs class variable
# class.__dict__ vs class_instance.__dict__


# difference between isntance, class and static methods

# class method vs static methods

# encapsulation
# abstraction
# inheritance
# polimorphism

# Class Method Examples
# 

# global state
class Employee:
    # Class-wide counter for the number of employees
    total_employees = 0

    def __init__(self, name, department):
        self.name = name
        self.department = department
        Employee.total_employees += 1

    def display_info(self):
        print(f"Name: {self.name}, Department: {self.department}")

    @classmethod
    def get_total_employees(cls):
        return cls.total_employees
      
# # Factory Methods
class EmployeeInfo:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def raise_salary(self, amount):
      self.salary += amount

    @classmethod
    def from_csv(cls, employee_row):
        fname, lname, salary = map(int, employee_row.split(","))
        return cls(fname, lname, salary)

    
      

# Factory Methods
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.damage} damage.")

    def display_info(self):
        print(
            f"Name: {self.name}, Health: {self.health}, Damage: {self.damage}")

    @classmethod
    def create_warrior(cls, name):
        return cls(name, health=100, damage=20)

    @classmethod
    def create_mage(cls, name):
        return cls(name, health=80, damage=30)

    @classmethod
    def create_archer(cls, name):
        return cls(name, health=90, damage=25)


# Usage
warrior = Character.create_warrior("Conan")
mage = Character.create_mage("Merlin")
archer = Character.create_archer("Robin Hood")


# Inheritance
    # able to use parent properties and methods in child class
    # able to change the properties and methods of parents without effecting the parent class
# Developer(Employee) and Manager(Employee)
# help(ClassName) function

# homework topic
# multiple inheritance
# multi level inhertance
# Hierarchical
# Hybrid

# from child class you can call the parent class init method in 2 ways
# super().__init__()
# MyClass().__init__()

# issubclass() function
# isinstance() function


# print( 1 + 2)  int.__add__(1, 2)
# print( "a" +  "b") # behind the scene -> str.__add__("a", "b")

# __repr__(self) -> for debugging
# __str__(self) -> for display  if str method doesn't exists then print(obj) will fall back to __repr__

# repr(obj)
# str(obj)

# __add__() # we can create this method in our class as well
# print( emp_1 + emp_2)
# datetime module also contains __add__ method and therefore we can write the code date1 + date2

# __len__


# encapsulation good example
# account: make balance private to prevent modifying the balance directly
# expose the methods depost and withdraw to modify the balance

# another example

# patient: make status private to prevent modifiying the statue directly from the code
# expose the method transfer
# expose the method discharge
# expose the method admit 
# to change the value of the status

# employee: make the salary private to prevent modifying the salary directly
# expose the method allowance, bonus, late to increase or decrease the salary amount



# create separate class for Manager, Developer explanation
# if employee types have significantly different behaviors, responsibilities, and attributes, it might be better to create separate classes for each type:

# benefit: 
# Modularity: Each employee type class can encapsulate its specific behavior, attributes, and responsibilities, making the code more modular and easier to maintain. This follows the Open-Closed Principle, allowing you to extend the system without modifying existing code.
# Clear Separation: It provides a clear separation of concerns. Each employee type class can focus on its unique logic without worrying about other types.


# polymorphism
# method overloading -> x
# method overriding -> yes

# calculate_salary()
# Developer has no allowance
# Manager has fuel_allowance

# calculate_annual_salary
# full time employee
# def calculate_annual_salary(self):
#         return self.monthly_salary * 12

# part time employee
# def calculate_annual_salary(self):
#     return self.hourly_rate * self.hours_worked_per_month * 12




# Abstraction
# sending email example



#exercise
