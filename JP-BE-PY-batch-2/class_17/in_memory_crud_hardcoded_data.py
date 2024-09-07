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