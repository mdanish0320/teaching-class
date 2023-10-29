import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="", # empty password
        db='sakila',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("db connected")
    return conn
    # cur = conn.cursor()
    # cur.execute("select @@version")
    # output = cur.fetchall()
    # print(output)

    # To close the connection
    

def disconnect(conn):
  conn.close()

# Driver Code
if __name__ == "__main__":
    mysqlconnect()
