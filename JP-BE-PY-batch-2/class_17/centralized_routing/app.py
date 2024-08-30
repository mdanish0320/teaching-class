from flask import Flask
from controller.create_user import create_user
from controller.get_user import get_single_user
from controller.get_all_users import get_all_users
from controller.get_all_users_posting import get_all_users_posting
from controller.delete_user import delete_user

app = Flask(__name__)

# root API of the application
@app.route("/", methods=['GET'])
def hello():
    return "centralized routing"

app.add_url_rule("/users", view_func=get_all_users, methods=['GET'])
app.add_url_rule("/users/<user_id>", view_func=get_single_user, methods=['GET'])
app.add_url_rule("/users/<user_id>", view_func=delete_user, methods=['DELETE'])
app.add_url_rule("/users", view_func=create_user, methods=['POST'])

app.add_url_rule("/users/<user_id>/posting", view_func=get_all_users_posting, methods=['GET'])

  
if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )

if __name__ == "__main__":
    app.run(debug=True, port=3000)
