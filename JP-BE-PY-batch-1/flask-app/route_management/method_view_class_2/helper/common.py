from functools import wraps

def token_required(func):
    @wraps(func)
    def _token_required(*args, **kwargs):
        print("before my_profile")
        data = {"id": 100}
        return func(data, *args, **kwargs)

    return _token_required