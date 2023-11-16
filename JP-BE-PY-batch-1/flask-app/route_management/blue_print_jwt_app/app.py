import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("flask-app")
from datetime import timedelta

# third party import
from flask import Flask
from flask.views import MethodView

# global configurations
app = Flask(__name__)

# jwt 
from flask_jwt_extended import JWTManager

# local imports
routers = []
from routes.employee import router_list as employee_route_list
from routes.user import router_list as user_route_list

routers.extend(employee_route_list)
routers.extend(user_route_list)



# https://flask-jwt-extended.readthedocs.io/en/stable/options.html
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["JWT_TOKEN_LOCATION"] = ["headers"] # specifying the location of JWT 
app.config["JWT_ALGORITHM"] = "HS256" # symmetric keyed hashing algorithm
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)

for route in routers:
    print(route)
    app.register_blueprint(route)

if __name__ == "__main__":

    app.run(
        debug=True,
        port=3000
    )
