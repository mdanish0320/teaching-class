# https://flask.palletsprojects.com/en/2.1.x/patterns/lazyloading/

from flask import Flask

from controller.mod_1 import func_1
from controller.mod_2 import func_2

app = Flask(__name__)

app.add_url_rule('/', view_func=func_1, methods=['GET'])
app.add_url_rule('/user/<idd>', 'dddd', view_func=func_2, methods=['POST'])

app.run(
  debug=True,
  port=3000
)