# Import necessary modules from Flask
from flask import Flask, Blueprint, request, jsonify
from flask.views import MethodView

# Create a Flask application
app = Flask(__name__)

# Create a Blueprint for the user service
user_bp = Blueprint('user', __name__)

# Sample data (for demonstration purposes)
users = [
    {'id': 1, 'name': 'John Doe'},
    {'id': 2, 'name': 'Jane Doe'},
]

# Define a class for the UserView with CRUD methods
class UserView(MethodView):
    def get(self, user_id=None):
        # Retrieve all users or a specific user by ID
        if user_id is None:
            return jsonify(users)
        else:
            user = next((user for user in users if user['id'] == user_id), None)
            if user:
                return jsonify(user)
            else:
                return jsonify({'error': 'User not found'}), 404

    def post(self):
        # Create a new user
        data = request.get_json()
        new_user = {'id': len(users) + 1, 'name': data['name']}
        users.append(new_user)
        return jsonify(new_user), 201

    def put(self, user_id):
        # Update an existing user by ID
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            data = request.get_json()
            user['name'] = data['name']
            return jsonify(user)
        else:
            return jsonify({'error': 'User not found'}), 404

    def delete(self, user_id):
        # Delete an existing user by ID
        global users
        users = [user for user in users if user['id'] != user_id]
        return jsonify({'result': True})

# Add the UserView class to the user blueprint with URL rules
user_bp.add_url_rule('/users', view_func=UserView.as_view('users'))
user_bp.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('user'))

# Register the user blueprint with the app
app.register_blueprint(user_bp)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=3000)
