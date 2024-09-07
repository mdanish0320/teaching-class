rom flask import Flask

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
