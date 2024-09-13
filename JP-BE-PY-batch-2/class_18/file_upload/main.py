import os
import uuid

from flask import Flask, request, abort

app = Flask(__name__)

# Get the current directory where main.py is located
basedir = os.path.abspath(os.path.dirname(__file__))

# Set the temporary upload directory (optional)
os.environ['UPLOAD_FOLDER'] = os.path.join(basedir, 'files/')


# root API
@app.route("/")
def hello():
    return "hello"


@app.route("/input/post/form-data/upload-file", methods=['POST'])
def input_post_form_data_upload_files():
    print(request.files)
    f = request.files['my_json_file']

    if not f: 
        abort(400, "No file uploaded")

    # Generate a unique filename
    # unique_filename = str(uuid.uuid4()) + '.json'
    
    file_path = os.environ['UPLOAD_FOLDER'] + 'single_file.json'
    f.save(file_path)

    return "success"

# research topic: how to handle multiple files uploading
# research topic: how to upload image file that is base64-encoded


if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )