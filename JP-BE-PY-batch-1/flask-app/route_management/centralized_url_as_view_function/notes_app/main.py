from flask import Flask
from routes.users import users_router_list
from routes.notes import notes_router_list

app = Flask(__name__)

# users routes
for route in users_router_list:
    app.register_blueprint(route)

# notes routes
for route in notes_router_list:
    app.register_blueprint(route)


if __name__  == "__main__":
    app.run(
        debug=True,
        port=3000
    )
