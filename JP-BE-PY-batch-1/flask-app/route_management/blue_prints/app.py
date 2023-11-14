import logging
logging.basicConfig(level=logging.DEBUG)

# third party import
from flask import Flask
from flask.views import MethodView

# local imports
from routes.employee import employee_bp

# global configurations
app = Flask(__name__)
log = logging.getLogger("flask-app")

app.register_blueprint(employee_bp)

if __name__ == "__main__":

    app.run(
        debug=True,
        port=3000
    )
