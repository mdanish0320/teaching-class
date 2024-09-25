from flask import Flask, request, make_response
app = Flask(__name__)



users = [
    {
        "id": 1,
        "email" : "danish@gmail.com", 
        "password" : "123"
    },
    {
        "id": 2,
        "email" : "fahad@gmail.com", 
        "password" : "123"
    }
]



"""
curl -X POST http://localhost:3000/signup \
-H "Content-Type: application/json" \
-d '{
  "id": "1",
  "email": "user@example.com",
  "password": "user_password"
}'
"""
@app.route("/signup", methods = ['POST'])
def create_user():
    # new_book = request.get_json()
    # users.append(new_book)
    return users


"""
curl -X POST http://localhost:3000/login \
-H "Content-Type: application/json" \
-d '{
  "email": "danish@gmail.com",
  "password": "1234"
}' \
-c cookies.txt
"""
@app.route("/login", methods=['POST'])
def login_user():
    data = request.get_json()
    for user in users:
        if user['email'] == data['email'] and user['password'] == data['password']:
            res = make_response("login successful")
            res.set_cookie(
                "user_id",
                str(user['id']),
                path="/",
                # httponly=True
            )
            return res
    return "incorrect user credentials"


"""
curl -X POST http://localhost:3000/logout \
-b cookies.txt -c cookies.txt
"""
@app.route("/logout", methods=['POST'])
def logout_user():
    res = make_response("logout successful")
    res.set_cookie("user_id", "", expires=0, path="/")
    return res


"""
curl -X GET http://localhost:3000/protected-api \
-b cookies.txt
"""
@app.route("/protected-api", methods=['GET'])
def protected_api_1():
    if request.cookies.get('user_id') is None:
        return "please login"
    
    return "protected data"

"""
curl -X GET http://localhost:3000/my-profile \
-b cookies.txt 
"""
@app.route("/my-profile", methods=['GET'])
def my_profile():
    if request.cookies.get('user_id') is None:
        return "please login"
    
    user_id = request.cookies.get('user_id')
    for user in users:
        if user['id'] == int(user_id):
            return user
    
    return "user not found"

app.run(debug=True, port=3000)