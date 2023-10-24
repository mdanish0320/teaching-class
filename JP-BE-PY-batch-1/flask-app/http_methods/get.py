from flask import Flask, request

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello"

@app.route("/input/get/query_string")
def user_input_with_query_string():
    print(request.args)
    print(request.args.get("x"))
    return "hello"


@app.route("/input/get/path_parameter/<name>/<name_2>")
def user_input_with_path_parameter(name, name_2):
    print("name", name)
    return "hello"

if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )