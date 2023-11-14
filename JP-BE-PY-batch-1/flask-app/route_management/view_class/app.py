from flask import Flask, jsonify, request
from flask.views import View

app = Flask(__name__)

class UserView(View):
    users = {
        "id": 1,
        "name": "danish"
    }  

    def __init__(self, db):
        self.x = 100
        self.db = db

    def dispatch_request(self, user_id=None):
        print("xxx", self.x)
        print("dddbb", self.db)
        if request.method == 'GET':
            return self.get(user_id)
        elif request.method == 'POST':
            return self.post()
        elif request.method == 'PUT':
            return self.put(user_id)
        elif request.method == 'DELETE':
            return self.delete(user_id)

    def get(self, user_id):
        if user_id in self.users:
            return jsonify(self.users[user_id])
        else:
            return jsonify(error="User not found"), 404

    def post(self):
        data = request.get_json()
        if 'id' in data and 'name' in data:
            user_id = data['id']
            self.users[user_id] = {'id': user_id, 'name': data['name']}
            return jsonify(self.users[user_id]), 201
        else:
            return jsonify(error="Invalid data"), 400

    def put(self, user_id):
        if user_id in self.users:
            data = request.get_json()
            self.users[user_id]['name'] = data['name']
            return jsonify(self.users[user_id])
        else:
            return jsonify(error="User not found"), 404

    def delete(self, user_id):
        if user_id in self.users:
            deleted_user = self.users.pop(user_id)
            return jsonify(deleted_user)
        else:
            return jsonify(error="User not found"), 404

# Add the view to the app with the associated route
app.add_url_rule('/user/<int:user_id>', view_func=UserView.as_view('user', 'db_url'))
app.add_url_rule('/user', view_func=UserView.as_view('users', 'db_url'))

if __name__ == '__main__':
    app.run(debug=True, port=3000)
