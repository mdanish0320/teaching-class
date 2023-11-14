import logging
logging.basicConfig(level=logging.DEBUG)

# third party import
from flask import Flask
from flask.views import MethodView

# local imports
# from routes.employee import employee_bp
from routes.employee import router_list

# global configurations
app = Flask(__name__)
log = logging.getLogger("flask-app")

c = 0
for route in router_list:
    c += 1
    app.register_blueprint(route, name=f"name{c}" )

if __name__ == "__main__":

    app.run(
        debug=True,
        port=3000
    )
