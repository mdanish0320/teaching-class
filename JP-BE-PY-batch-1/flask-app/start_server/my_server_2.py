from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! from my_server_22.py</p>"

# run application server by running following command
# python3 my_server_2.py

if __name__ == '__main__':
   app.run()


# debug=True, # hot reload
# host='localhost'
# port=5001
