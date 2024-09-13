from flask import Flask, jsonify, Response, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/error')
def error_example():
    return 'Not Found', 404


@app.route('/custom')
def custom_response():
    return 'Custom Response', 200, {'X-Custom-Header': 'Value'}


@app.route('/data')
def get_data():
    data = {'key': 'value'}
    return jsonify(data)



@app.route('/response')
def custom_response_object():
    # entire response object in one go.
    return Response('Custom Response Object', status=200, mimetype='text/plain')


@app.route('/json_make_response')
def json_make_response():
    data = {'key': 'value'}
    response = make_response(jsonify(data))
    response.headers['X-Custom-Header'] = 'Value'
    return response



if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )