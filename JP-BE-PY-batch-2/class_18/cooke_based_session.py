from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/")
def root():
    return "cookie based session example"

@app.route('/set_cookie')
def set_cookie():
    # Create the response object using make_response
    response = make_response('Cookie has been set')

    # Set the HTTP-only cookie
    response.set_cookie(
        'session_id',        # Cookie name
        '123456789',         # Cookie value
        httponly=True,       # Ensure the cookie is HTTP-only
        max_age=3600,        # Cookie expiration time (in seconds)
        # secure=True,         # Ensure the cookie is only sent over HTTPS
        path='/',            # Path where the cookie is valid
        samesite='Lax'       # SameSite policy
    )

    # Return the response object
    return response

@app.route('/get_cookie')
def get_cookie():
    # Get the session_id cookie from the request
    session_id = request.cookies.get('session_id', 'Cookie not found')

    return f'Session ID: {session_id}'

if __name__ == '__main__':
    app.run(debug=True, port=3000,) 


"""
Effect of Path on Requests:

With path='/', the cookie will be sent with requests to /user/profile, /admin, and any other subpath.
With path='/user', the cookie will only be sent with requests to /user/profile, /user/settings, but not /admin or /about.
"""
