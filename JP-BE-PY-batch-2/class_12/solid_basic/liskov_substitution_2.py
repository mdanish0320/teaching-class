"""
L - Liskov Substitution Principle (LSP):

Objects of a superclass should be replaceable with objects of a subclass 
without affecting the correctness of the program. 

In other words, subclasses should be substitutable for their base classes 
without altering the desirable properties of the program (e.g., correctness, task performed, etc.).
"""

from abc import ABC, abstractmethod

# before
class Bird(ABC):
    @abstractmethod
    def eat():
        pass

    @abstractmethod
    def fly():
        pass

class Sparrow(Bird):
    def eat():
        print("Sparrow is eating")

    def fly():
        print("Sparrow is flying")

class Peacock(Bird):
    def eat():
        print("Peacock is eating")

    def fly():
        print("Peacock is flying")


class Ostrich(Bird):
    def eat():
        print("Ostrich is eating")

    def fly():
        raise Exception("Ostrich cannot fly")
    


# before
class Bird(ABC):
    @abstractmethod
    def eat():
        pass

class IFlyingBird(Bird):
    @abstractmethod
    def fly():
        pass

class Sparrow(IFlyingBird):
    def eat():
        print("Sparrow is eating")

    def fly():
        print("Sparrow is flying")

class Peacock(IFlyingBird):
    def eat():
        print("Peacock is eating")

    def fly():
        print("Peacock is flying")


class Ostrich(Bird):
    def eat():
        print("Ostrich is eating")
