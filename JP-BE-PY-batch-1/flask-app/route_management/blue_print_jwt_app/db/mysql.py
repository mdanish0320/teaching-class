import pymysql

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="", # empty password
        db='test_db_1',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("db connected")
    return conn

def disconnect(conn):
  conn.close()
