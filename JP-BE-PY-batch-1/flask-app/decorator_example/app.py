from functools import wraps
import jwt
from flask import Flask, request
app = Flask(__name__)

SECRET_KEY = "ABCD123"

def token_required(func):
    @wraps(func)
    def _token_required(*args, **kwargs):
        print("before my_profile")
        token = request.args.get("token")
        print('token', token)
        
        # verify token
        user=jwt.decode(
            token, 
            SECRET_KEY, 
            algorithms=["HS256"]
        )
        print("user", user)
        response =  func(user, *args, *kwargs)
        print("after my_profile")

        return response
    return _token_required


@app.route("/")
def home():
    return "home"


@app.route("/login")
def login():
    # create token
    token = jwt.encode(
        {"user_id": "123"},
        SECRET_KEY,
        algorithm="HS256"
    )
    print(token)
    return token

# http://localhost:3000/my_profile?token=eyJ0eXAiOiJ......
@app.route("/my_profile")
@token_required
def my_profile(data):
    print('data',data)
    return "my_profile"


app.run(
    debug=True,
    port=3000
)