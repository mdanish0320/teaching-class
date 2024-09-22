from controller.api_blueprint import auth_bp
from controller.auth import signup,login,logout_user

# Add URL rule to the blueprint
auth_bp.add_url_rule('/signup', view_func=signup, methods=['POST'])
auth_bp.add_url_rule('/login', view_func=login, methods=['POST'])
auth_bp.add_url_rule('/logout', view_func=logout_user, methods=['POST'])