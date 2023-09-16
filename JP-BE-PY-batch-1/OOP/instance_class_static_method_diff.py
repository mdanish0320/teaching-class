## Instance Method
# Must have first parameters self
# Can access self and class level attribute and static method

## Class Method
# Use decorator, @ classmethod
# Must have first parameters cls
# Inside class method, you can only access class level attributes and class level methods and static method

## Static Method
# Use decorator, @ staticmethod
# No parameter required
# static method cannot use self and cls as an argument.
# to invokce static method, use syntax -> classname.static_method()
