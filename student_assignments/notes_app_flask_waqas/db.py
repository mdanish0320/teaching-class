import os
import pymysql

def mysqlconnection():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        db='notes',
        # password=os.getenv('password'),
        password='',
        cursorclass=pymysql.cursors.DictCursor,
    )
    print('db connected')
    return conn


def diconnect(conn):
    conn.close()
    

if __name__=='__main__':
    mysqlconnection()    
