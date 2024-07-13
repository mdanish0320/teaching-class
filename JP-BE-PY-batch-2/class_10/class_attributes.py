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
    # this is the class level attributes (shared among the objects)
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
