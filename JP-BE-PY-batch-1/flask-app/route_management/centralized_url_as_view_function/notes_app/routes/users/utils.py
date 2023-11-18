def validate_user_data(data):
    error_msg = None
    if data.get("name") is None or len(data.get("name").strip()) == 0:
        error_msg = "name field is required"
    elif data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"
    elif data.get("password") is None or len(data.get("password").strip()) == 0:
        error_msg = "password field is required"
    return error_msg

def validate_login_data(data):
    error_msg = None
    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"
    elif data.get("password") is None or len(data.get("password").strip()) == 0:
        error_msg = "password field is required"
    return error_msg