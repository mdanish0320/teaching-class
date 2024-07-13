"""
what is self?

self is a conventional name for the first parameter of instance methods in a class. 
It represents the instance of the class itself 
and allows access to the instance's attributes and methods.
"""
class RegistrationForm():
    def __init__(self):
        print(self)
        self.first_name = "muhammad"
        self.last_name = "danish"

obj = RegistrationForm()
print(obj)
print(
    obj.__dict__
)