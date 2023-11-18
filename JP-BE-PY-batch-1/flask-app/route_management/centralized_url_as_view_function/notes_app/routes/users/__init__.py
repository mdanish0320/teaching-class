from .add_new_user import user_bp as add_user_bp
from .login_user import user_bp as login_user_bp

users_router_list = []
users_router_list.append(add_user_bp)
users_router_list.append(login_user_bp)