# 3 important things

# 1. properties
# 2. behavour
# 3. constructor/desctructor

# there is no big difference in both as per our examples
### create program to display the difference between procedural and OOP
### force on 3 points
### 1. code readablility
### 2. code complexity
### 3. state management: global state vs individutal object state

# write a program in procedural way
# tell students to covert the logic in OOP


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
