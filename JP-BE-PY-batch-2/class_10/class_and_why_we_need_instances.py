# creating class without attributes
class JPPythonRegistrationForm:
    pass

JPPythonRegistrationForm.fname = "muhamad"
JPPythonRegistrationForm.lname = "danish"
print(JPPythonRegistrationForm.fname)
print(JPPythonRegistrationForm.lname)

JPPythonRegistrationForm.fname = "Fahad"
JPPythonRegistrationForm.lname = "Ali"
print(JPPythonRegistrationForm.fname)
print(JPPythonRegistrationForm.lname)

# its running like a single and global dictionay
# we have a single form and everyone overwrites it
# therefore we need object or instance variable


# adding dynamic attributes in the above class
obj_1 = JPPythonRegistrationForm()
obj_1.fname = "muhammad"
obj_1.lname = "danish"

obj_2 = JPPythonRegistrationForm()
obj_2.fname = "muhammad"
obj_2.lname = "danish"

# memory address of the object
print(obj_1)

# class stores the attributes internallly as hashmap
print(
    obj_1.__dict__
)

# now we have multiple copies of the Registration Form
# but still we need template form

# creating a template registration form
class RegistrationForm():
    def __init__(self):
        self.first_name = "muhammad"
        self.last_name = "danish"

obj = RegistrationForm()
print(
    obj.__dict__
)


# creating a template registration form
class RegistrationForm():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

obj = RegistrationForm("muhammad", "danish")
print(
    obj.__dict__
)
