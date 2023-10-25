from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run(
        port=3000,
        debug=True
    )

## run blow command on terminal to start the server
# gunicorn -w 4 'flask_app:app'