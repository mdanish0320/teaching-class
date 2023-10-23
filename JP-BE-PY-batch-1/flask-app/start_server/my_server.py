from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! from my_server.py</p>"

# run application server by running following command
# flask --app my_server run
