def my_decorator_func(func):
    def wrapper_func(*args, **kwargs):
        print("before home page")
        func("danish", *args, **kwargs)
        print("after home page")
    return wrapper_func


@my_decorator_func
def home(data):
    print("home page", data)

home()