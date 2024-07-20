from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "eating meal")

    def sleep(self):
        print(self.name, "sleeping ZzzZzZzz")

    # common animal behavour/method
    @abstractmethod
    def move(self):
        pass
    


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    # dog specific behavour/method
    def play_with_stick(self):
        print(self.name, "bringing stick")

    # common animal behavour/method
    def move(self):
        print(self.name, "walking in 4 legs")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    # cat specific behavour/method
    def climb(self):
        print(self.name, "climbing the tree")
      
    # common animal behavour/method
    def move(self):
        print(self.name, "walking in 4 legs")
    

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    # common animal behavour/method
    def move(self):
        print(self.name, "swiming")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)


dog = Dog("dog")
dog.eat()
# dog.climb()
dog.play_with_stick()
dog.move()

print("--------")
cat = Cat("cat")
cat.eat()
cat.climb()
# cat.play_with_stick()
cat.move()


fish = Animal("Fish")
fish.move()

bird = Bird("bird")
bird.move()