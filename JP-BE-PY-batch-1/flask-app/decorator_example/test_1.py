def my_decorator_func(func):
    def wrapper_func():
        print("before home page")
        func()
        print("after home page")
    return wrapper_func


@my_decorator_func
def home():
    print("home page")

home()