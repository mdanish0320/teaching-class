from flask import Flask, request

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello"

@app.route("/input/post/form-data", methods=['POST'])
def input_post_form_data():
    print(request.form)
    print(request.form.get("name"))
    return "hello"

@app.route("/input/post/form-urlencoded", methods=['POST'])
def input_post_form_url_encoded():
    print(request.form)
    print(request.form.get("name"))
    return "hello"


@app.route("/input/post/json", methods=['POST'])
def input_post_raw():
    data = request.get_json()
    print(data)
    print(data.get("name"))
    return data


@app.route("/input/post/form-data/upload-file", methods=['POST'])
def input_post_form_data_upload_files():
    import os
    
    print(request.files)
    print(request.form)
    
    f = request.files['my_json_file']
    cwd = os.getcwd() # /Users/danish/teaching-class/JP-BE-PY-batch-1/flask-app/http_methods
    # print(f.read())
    f.save(cwd + "/files/single_file.json")
    return "hello"


@app.route("/input/post/form-data/upload-multiple-files", methods=['POST'])
def input_post_form_data_upload_multiple_files():
    import os
    cwd = os.getcwd() # /Users/danish/teaching-class/JP-BE-PY-batch-1/flask-app/http_methods
    print(request.files)
    print(request.form)
    files = request.files.getlist("my_json_file")
    for f in files:
        print(f.filename)
        f.save(cwd + "/files/" + f.filename)
    return "hello"

if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )
