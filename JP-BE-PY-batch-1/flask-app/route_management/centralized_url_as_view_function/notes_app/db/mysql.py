import pymysql


def connect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='google_notes',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def disconnect(conn):
  conn.close()