"""
if a class contains only abstract methods and no concrete methods, 
it effectively serves as an interface. 

On the other hand, if a class contains at least one abstract method and at least one concrete method, 
it is considered an abstract class. Here's a clearer distinction
"""


"""
Python does not have a built-in interface keyword like Java. 
However, similar behavior can be achieved using abstract base classes:

Interface-like Class in Python
A class with only abstract methods:
"""
from abc import ABC, abstractmethod

class InterfaceExample(ABC):
    @abstractmethod
    def method1(self):
        pass
    
    @abstractmethod
    def method2(self):
        pass

# Example implementation
class ConcreteClass(InterfaceExample):
    def method1(self):
        print("Method 1 implemented")
    
    def method2(self):
        print("Method 2 implemented")
        
        
"""
Abstract Class in Python
A class with at least one abstract method and one concrete method:
"""
from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    @abstractmethod
    def method1(self):
        pass
    
    def concrete_method(self):
        print("This is a concrete method")

# Example implementation
class ConcreteClass(AbstractClassExample):
    def method1(self):
        print("Method 1 implemented")

