# how to create class
# how to create instance
# each instance have its own properties
# dynamic attributes

# instance attributes
# self
# class attributes
# why cannot we use class attribute intead of instance attribute
# instance method

class MyClass:
  # class attribute
  phone_num = "0320-2565654"
  
  # instance attribute
  # self
  # jawan pak admission form
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
    
  # def get_fullname(self):
  #   pass
  
  @classmethod
  def get_fullname(cls):
    pass
  

instance_1 = MyClass("muhammad", "danish")
instance_2 = MyClass("fahad", "ali")
instance_3 = MyClass("shoaib", "soomro")

# each instance have its own properties
# dynamic attribute
instance_1.abc = "abc"
instance_2.abc = "123"
instance_3.xyz = "xyz"

print(
  instance_1.__dict__,
  instance_2.__dict__,
  instance_3.__dict__,
)

print(MyClass.__dict__)
print(instance_1.phone_num)

MyClass.phone_num = "121235"
print(instance_1.phone_num)