# method find
"""
Definition: The find() method finds the first occurrence of the specified value.
            It returns the position number couting from the left.
            The find() method returns -1 if the value is not found.
"""


txt = "hello world"
index_number = txt.find("world")

print(index_number) # 6



txt = "hello world"
index_number = txt.find("hello")

print(index_number) # 0


txt = "hello world"
index_number = txt.find("godzilla")

print(index_number) # -1

