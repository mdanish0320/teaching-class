from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! from app.py...</p>"

# run application server by running following command
# flask run
# OR
# flask run --host localhost --port 7000

