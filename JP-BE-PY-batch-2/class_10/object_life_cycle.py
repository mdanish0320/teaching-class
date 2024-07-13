class MyClass:
    
    def __new__(cls):
         print("Creating instance")
         return super(MyClass, cls).__new__(cls)

    def __init__(self):
        print("Init is called")
        
    def __str__(self):
        return f"MyClass id:{self.id}"
    
    # destructor
    def __del__(self):
        print("deleting the object")
    

obj = MyClass()

obj.id = 100
print(obj)
obj = None
print("abcd")