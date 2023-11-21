from flask import Flask
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.username())

@app.route('/data')
@auth.login_required
def indexx():
    return "Hello, {}!".format(auth.username())

if __name__ == '__main__':
    app.run(
        port=3000,
        debug=True
    )