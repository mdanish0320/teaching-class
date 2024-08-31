from flask import Flask

app = Flask(__name__)

# root API of the application
@app.route("/", methods=['GET'])
def hello():
    return "root of the application"


# users APIs
@app.route("/users", methods=['GET'])
def all_users():
    return "all users"

@app.route("/users/1", methods=['GET'])
def one_user():
    return "one user data only"

@app.route("/users/1", methods=['PUT'])
def update_user():
    return "update user"

@app.route("/users/1", methods=['PATCH'])
def update_minor_user():
    return "update 1 piece of info of user"

@app.route("/users/1", methods=['DELETE'])
def delete_user():
    return "create new user"

@app.route("/users", methods=['POST'])
def new_user():
    return "create new user"

if __name__ == "__main__":
    app.run(debug=True, port=3000)
