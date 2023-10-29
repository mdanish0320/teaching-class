import json

from flask import Flask

import db

app = Flask(__name__)

@app.route("/api_1", methods=['GET'])
def api_1():
    # create connection with db
    db_conn = db.mysqlconnect()
    
    # fetch data from db
    query = "SELECT * FROM language"
    cur = db_conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    
    # close connection with databse
    db.disconnect(db_conn)
    
    # api response
    return data
  

@app.route("/api_2", methods=['POST'])
def api_2():
    # create connection with db
    db_conn = db.mysqlconnect()

    # add record into databse
    query = "INSERT INTO language VALUES (7, 'abc', '2006-02-15 05:02:19')"
    cur = db_conn.cursor()
    cur.execute(query)
    
    # save the changes permanently
    db_conn.commit()

    # close connection with databse
    db.disconnect(db_conn)

    # api response
    return "data added successfully"


if __name__ == "__main__":
    app.run(
        port=3000,
        debug=True
    )
