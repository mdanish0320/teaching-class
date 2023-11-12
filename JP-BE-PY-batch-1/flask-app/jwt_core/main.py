import jwt
from flask import Flask, request
app = Flask(__name__)


users = [{
    "id": 1,
    "name": "danish",
    "email": "danish@gmail.com",
    "password": "1234"
}]

SECRET = "ABCD123"

# http://localhost:3000/login
@app.route("/login", methods=['POST'])
def login():

    input = request.get_json()
    email = input.get("email")
    password = input.get("password")

    for u in users:
        if u['email'] == email and u['password'] == password:
            token_data = {
                "id": u['id'],
                "email": u['email']
            }
            # create a new pass
            token = jwt.encode(
                token_data,
                SECRET,
                algorithm="HS256"            )
            return token, 200
    else:
        return {"message": "user not found"}, 200

#http://localhost:3000/my_profile?token=eyJhb.....
@app.route("/my_profile", methods=['GET'])
def my_profile():
    # validate the pass (security guard)
    token = request.args.get("token")
    print("tokenn", token)
    decoded_token = jwt.decode(
        token,
        SECRET,
        algorithms="HS256"
    )
    print("decoded_token", decoded_token)
 

    for u in users:
        if u['id'] == decoded_token['id']:
            return u, 200
   


app.run(
    debug=True,
    port=3000
)