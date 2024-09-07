# main.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"


app.run(
    debug=True,
    port=3000
)


@app.route("/users")
def get_all_users():
    return "all users"

@app.route("/users/100")
def get_all_users():
    return "all users"


@app.route("/users/100/post")
def get_all_users():
    return "all users"

@app.route("/users/100/posts/6")
def get_all_users():
    return "all users"


@app.route("/post")
def get_all_users():
    return "all users"

app.run(
    debug=True,
    port=3000
)









# main_2.py

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello"

@app.route("/users", methods=['POST'])
def create_user():
    return "create user"

@app.route("/users", methods=['GET'])
def get_all_users():
    return "all users"

app.run(
    debug=True,
    port=3000
)








# main_3.py


from flask import Flask

app = Flask(__name__)


users = []
print("hello  worldd")

@app.route("/")
def hello():
    return "hello"

@app.route("/users", methods=['GET'])
def get_all_users():
    return users


@app.route("/users", methods=['POST'])
def create_user():
    users.append({"id": 1, "name": "danish"})
    return users


@app.route("/users/1", methods=['PUT'])
def update_user():
    for u in users:
        if u['id'] == 1:
            u['name'] = "fahad"
    return users



app.run(
    debug=True,
    port=3000
)









# main_4.py


from flask import Flask, request

app = Flask(__name__)


users = []
print("hello  worldd")

@app.route("/")
def hello():
    return "hello"

# query string
# http://localhost:3000/users?status=1&limit=10&order=asc
@app.route("/users", methods=['GET'])
def get_all_users():
    print(request.args)
    params = request.args
    print("status_value", params['status'])
    return users

# path parameter
@app.route("/users/<id>", methods=['GET'])
def get_single_users(id):
    print('id', id)
    return users

# raw data

def create_user():
    # categorti = input("entert category name")
    data = request.get_json()
    category = data['category_name']
    db.connect()

    query.add_category(category)
    data = request.get_json()
    print(data)
    users.append({"id": 1, "name": "danish"})
    db.disconnect()
    return users



# @app.route("/users/1", methods=['PUT'])
# def update_user():
#     for u in users:
#         if u['id'] == 1:
#             u['name'] = "fahad"
#     return users



app.run(
    debug=True,
    port=3000
)