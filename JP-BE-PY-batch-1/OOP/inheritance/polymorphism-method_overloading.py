## add 1 new method
# make_sound() # NOTE: every animal has unique sound


class Animal():
    # instance attributes
    def __init__(
        self,
        name,
        breed,
        is_litter_box_trained,
        price
    ):
        self.name = name
        self.breed = breed
        self.is_litter_box_trained = is_litter_box_trained
        self.price = price
        
        # self.age = ""
        # self.color = ""

    # instance methods
    def eat(self):
        print(
            f"{self.name}: yum yum eating meal"
        )

    def sleep(self):
        print(
            f"{self.name}: ZzZzZzZzZ"
        )

    def move(self):
        print(
            f"{self.name}: walking with 4 legs"
        )

    def play(self):
        print(
            f"{self.name}: running in circles"
        )
        
    # new method
    def make_sound(self):
      pass


class Dog(Animal):
    def __init__(self,
                 name,
                 breed,
                 is_litter_box_trained,
                 price):
        super().__init__(name, breed, is_litter_box_trained, price)

    def fetch(self):
        print(
            f"{self.name}: bring back the stick"
        )
    # new method
    # method overriding
    def make_sound(self):
        print(
            f"{self.name}: woof woof"
        )


class Cat(Animal):
    def __init__(self,
                 name,
                 breed,
                 is_litter_box_trained,
                 price):
        super().__init__(name, breed, is_litter_box_trained, price)

    def climb(self):
        print(
            f"{self.name}: climb up the tree"
        )
        
    # new method
    # method overriding
    def make_sound(self):
        print(
            f"{self.name}: meow meow"
        )


cat = Cat("cat 1", "cat breed 1", True, 1000)
dog = Dog("dog 1", "dog breed 1", False, 2000)

cat.move()
dog.move()

cat.sleep()
dog.sleep()

cat.eat()
dog.eat()

cat.play()
dog.play()

print("-------------------------")

cat.climb()
dog.fetch()


print("-------------------------")
cat.make_sound()
dog.make_sound()
