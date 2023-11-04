from flask import Flask
import pymysql

app = Flask(__name__)

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="", # empty password
        db='hr_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("db connected")
    return conn
    
def disconnect(conn):
  conn.close()

@app.route("/")
def home():
   return "home page"


@app.route("/connect-db")
def connect_db():
   
   db = mysqlconnect()
   disconnect(db)

   return "db connection"


# Driver Code
if __name__ == "__main__":
    app.run(
       debug=True,
       port=3000
    )


# ----------------------------------------------------------------------------------------------
## create database
# find the button "Databases" and click
# you will see the form that requires you to enter mysql password, fill the form and hit the button "initialize Mysql". Store the password in safe place
# now you can find the following info in mysql settings i.e host, username and database
# database name would be something like "{YOUR_ACCOUNT_NAME}$default"
# NOTE: you can create more database if you like, every database you create will get prefixed by your account name following by a dollar sign

## create tables in the database
# find the button "Files" on the top and click
# find the button "mysite" and click enter
# create a folder "databases" and inside it upload database of "db.sql"
# find the button "Databases" and click
# create a new database
# click on your database name. It will open up a new terminal and mysql client will be running by default
# type the following command "SOURCE mysite/database/db.sql"
# type the following command to confirm if db is imported successfully: "SHOW tables;"
