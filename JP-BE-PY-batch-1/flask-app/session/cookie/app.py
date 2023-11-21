from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/profile")
def my_profile():
    user_id = request.cookies.get('logged_in_user')
    if user_id is None:
        return "please login"
    return "my profile" + user_id


@app.route("/login")
def login():
    user_id = request.cookies.get('logged_in_user')
    if user_id is not None:
        return "already login"
    
    res = make_response("logged in")
    res.set_cookie('logged_in_user', '100')
    return res

@app.route("/logout")
def logout():

    request.set_cookie('logged_in_user', '', expires=0)
    return "logged out"


app.run(
    port=3000,
    debug=True
)