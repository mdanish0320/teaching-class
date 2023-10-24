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


@app.route("/input/post/raw", methods=['POST'])
def input_post_raw():
    data = request.get_json()
    print(data)
    print(data.get("name"))
    return data


@app.route("/input/post/form-data/upload-files", methods=['POST'])
def input_post_form_data_upload_files():
    import os
    
    print(request.files)
    f = request.files['my_json_file']
    cwd = os.getcwd() # /Users/danish/teaching-class/JP-BE-PY-batch-1/flask-app/http_methods
    # print(f.read())
    f.save(cwd + "/files/file_3.json")

    

    return "hello"

if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )