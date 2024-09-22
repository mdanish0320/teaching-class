from flask import Blueprint

from controller.auth import signup, login, logout

#create a auth module blueprint
auth_bp = Blueprint('auth', __name__)

# Add URL rule to the blueprint
auth_bp.add_url_rule('/signup', view_func=signup, methods=['POST'])
auth_bp.add_url_rule('/login', view_func=login, methods=['POST'])
auth_bp.add_url_rule('/logout', view_func=logout, methods=['POST'])