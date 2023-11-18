from flask import request
import jwt


SECRET = "ABCD123"


def token_decrypt(func):
    def _token_decrypt(*args, **kwargs):
        decoded_data = None
        try:
            token = request.args.get("token")
            if token is None: raise Exception
            decoded_data = jwt.decode(token, SECRET, algorithms="HS256")
        except:
            return {"error": {"message": "Unauthenticated user"}}
        print(decoded_data)
        return func(decoded_data["id"], *args, **kwargs)
    _token_decrypt.__name__ = func.__name__
    return _token_decrypt


def enrypt(user_id):
    token = jwt.encode({"id": user_id}, SECRET, algorithm="HS256")
    return token
