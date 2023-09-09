# topic OOP

## explaination
# class keyword
# class name is PascalCase
# dynamic attributes (not shared between objects)
# instance attributes (not shared between objects)
# class level attributes (shared between objects)
# class initialization
# constructor/desctructor
# instanace method
# self keyword

# creating class without attributes
class MyClass():
    pass

# adding dynamic attributes in the above class
obj = MyClass()
obj.fname = "muhammad"
obj.lname = "danish"
print(
    obj.__dict__
)

# creating class with attributes
class MyClass():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

obj = MyClass("muhammad", "danish")
print(
    obj.__dict__
)

# create method in class
class MyClass():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_fullname(self):
        return self.first_name +" "+ self.last_name

obj = MyClass("muhammad", "danish")
print(
    obj.get_fullname()
)

# create 2 objects on the same class
class MyClass():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_fullname(self):
        return self.first_name + " " + self.last_name


obj_1 = MyClass("muhammad", "danish")
print(
    obj_1.get_fullname()
)
obj_2 = MyClass("fahad", "soomro")
print(
    obj_2.get_fullname()
)

# create 2 objects on the same class and see if adding new dynamic attribute in one object visible on other
class MyClass():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_fullname(self):
        return self.first_name + " " + self.last_name


obj_1 = MyClass("muhammad", "danish")
obj_1.salary = 2000 # dynamic attribute
print(
    obj_1.__dict__
)
obj_2 = MyClass("fahad", "soomro")
print(
    obj_2.__dict__
)



# class level attributes (shared)
class MyClass():
    counter = 0 # this is the class level attributes (shared amonth the objects)
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_fullname(self):
        return self.first_name + " " + self.last_name


# accessing class level attributes
# remember, to access class level attributes you don't need to create instance
print(
    MyClass.counter
)


# Modifying Class level attributes
class MyClass():
    # this is the class level attributes (shared amonth the objects)
    counter = 0

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_fullname(self):
        return self.first_name + " " + self.last_name

obj_1 = MyClass("muhammad", "danish")
print(
    obj_1.counter # it should display 0
)
MyClass.counter = 100
print(
    obj_1.counter  # it should display 100
)


# Modifying Class level attributes in instance
class MyClass():
    # this is the class level attributes (shared amonth the objects)
    counter = 0

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_fullname(self):
        return self.first_name + " " + self.last_name


obj_1 = MyClass("muhammad", "danish")
print(
    obj_1.counter  # it should display 0
)
obj_1.counter = 300 # changing class level attribute in instance
print(
    obj_1.counter  # it should display 300
)

obj_2 = MyClass("fahad", "soomro")
print(
    obj_2.counter  # it should display 0, above instance changes didn't reflect here
)


# challenge
class MyClass():
    # this is the class level attributes (shared amonth the objects)
    employee_count = 0

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.employee_count += 1

