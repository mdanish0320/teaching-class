from flask import Flask

app = Flask(__name__)


@app.route("/")
def my_app():
    return "My Application"

@app.route("/hello")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run(
        port=3000,
        debug=True
    )

## open your browser
# go to: https://www.pythonanywhere.com/
# find the button signup on the top and click
# find the button "Create a Beginner Account" and click
# You will see the Create Account Form, provide the details

## after successfully creating the account, you will see the dashboard page
# find the button "Web" on the top and click
# find the button "Add a new web app" in left menu
# click next and then click on Flask and then use version Python 3.8 and click next

## at this point, your new web application environment is setup and now you have to upload your files
# find the button "Files" on the top and click
# find the button "mysite" on left menue and click
# remove the file "flask_app.py"
# upload your file "main.py" and "requirements.txt"

# Now go back to the page "Web"
# find the word "WSGI Configuration file:" and click on the link next to it
# update the last line of the *_wsgi.py file 
# replace "flask_app" to "main" and click on the save button
# Now go back to the page "Web" and find the text "Reload:" and click that green reload button
# Find the text "Configuration for" and click on the link next to it to view your web app

# NOW YOU CAN SEE YOUR web application is LIVE


# ----------------------------------------------------------------------------------------------
## install modules in your new web application
# find the button "Consoles" on the top and click
# find the text "Other:" and click the link "Bash". You will see the black screen terminal
# enter into the directory mysite by typing "cd mysite"
# create virtualenv by following command "virtualenv venv --python=python3.8"
# activate the virtualenv by following command "source venv/bin/activate"
# install your modules by following command "pip3 install -r requirements.txt"
# Now go back to the page "Web"
# find the section "Virtualenv" and add your environment path i.e "/home/{YOUR_ACCOUNT_NAME}/mysite/venv"
# find the text "Reload:" and click that green reload button
# Find the text "Configuration for" and click on the link next to it to view your web app