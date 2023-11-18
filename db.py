import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='google_notes',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("db connected")
    return conn

def disconnect(conn):
  conn.close()