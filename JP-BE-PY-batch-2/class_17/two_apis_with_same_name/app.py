from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "hello"

@app.route("/", methods=['GET'])
def world():
    return "world"

if __name__ == "__main__":
    app.run(debug=True, port=3000)


"""
debug=True enables debug mode, which provides detailed error messages and automatic reloading of the server when code changes.

app = Flask(__name__)
__name__: This is a special Python variable that holds the name of the current module (the script you're running).
When you pass __name__ to the Flask class, it tells Flask where to look for resources like templates and static files. It also helps Flask to determine the root path of your application.

"""