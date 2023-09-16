## add 2 new methods
# climb() # NOTE: only cat can climb the tree and dog cannot
# fetch() # NOTE: only god can fetch the stick and cat cannot

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
        
    # new methods
    def climb(self):
        print(
            f"{self.name}: climb up the tree"
        )
    
    # new methods
    def fetch(self):
        print(
            f"{self.name}: bring back the stick"
        )


cat = Animal("cat 1", "cat breed 1", True, 1000)
dog = Animal("dog 1", "dog breed 1", False, 2000)

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
dog.climb() # its wrong

cat.fetch() # its wrong
dog.fetch()
