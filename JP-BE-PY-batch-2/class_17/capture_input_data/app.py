from flask import Flask, request

app = Flask(__name__)

# root API of the application
@app.route("/", methods=['GET'])
def hello():
    return "root of the application"


@app.route("/input/get/query_string")
def user_input_with_query_string():
    print(request.args)
    return "success:query_string"


@app.route("/input/get/path_parameter/<user_id>")
def user_input_with_path_parameter(user_id):
    print("user_id", user_id)
    return "success:path_parameter"
  

@app.route("/input/post/form-data", methods=['POST'])
def input_post_form_data():
    print(request.form)
    return "success:form-data"


@app.route("/input/post/form-urlencoded", methods=['POST'])
def input_post_form_url_encoded():
    print(request.form)
    return "success:form-urlencoded"


@app.route("/input/post/json", methods=['POST'])
def input_post_raw():
    data = request.get_json()
    return data
  
if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )

if __name__ == "__main__":
    app.run(debug=True, port=3000)
