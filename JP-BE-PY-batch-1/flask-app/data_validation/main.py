from flask import Flask, request

app = Flask(__name__)

@app.route("/add/employee", methods=['POST'])
def input_post_raw():
    data = request.get_json()
    return data


if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )
