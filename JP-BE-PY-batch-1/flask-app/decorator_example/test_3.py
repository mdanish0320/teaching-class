import jwt
from functools import wraps

SECRET_KEY = "ABCD123"


def token_required(func):
    @wraps(func)
    def _token_required(*args, **kwargs):
        print("before my_profile")
        print(args)
        print(kwargs)
        # verify token
        data=jwt.decode(
            args[0], 
            SECRET_KEY, 
            algorithms=["HS256"]
        )
        func(data)
        print("after my_profile")
    return _token_required


@token_required
def my_profile(data):
    print("my_profile")


def login():
    # create token
    token = jwt.encode(
        {"user_id": "123"},
        SECRET_KEY,
        algorithm="HS256"
    )
    print(token)
    return token

token = login()
my_profile(token)