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
