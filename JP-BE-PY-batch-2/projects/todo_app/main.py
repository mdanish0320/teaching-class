from flask import Flask, render_template
from flask_cors import CORS

from controller.user.signup import signup
from controller.user.login import login
from controller.user.logout import logout
from controller.task.all_tasks import get_all_tasks

app = Flask(__name__)
CORS(app)

# authentication
app.add_url_rule("/users/signup", view_func=signup, methods=['POST'])
app.add_url_rule("/users/login", view_func=login, methods=['POST'])
app.add_url_rule("/users/logout", view_func=logout, methods=['POST'])

# tasks
app.add_url_rule("/tasks", view_func=get_all_tasks, methods=['GET'])

@app.route("/")
def root():
  return "todo app"

if __name__ == "__main__":
  app.run(debug=True, port=3000)