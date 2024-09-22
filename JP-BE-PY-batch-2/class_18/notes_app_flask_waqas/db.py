import os
import pymysql

def mysqlconnection():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        db='waqas_notes_app',
        cursorclass=pymysql.cursors.DictCursor,
    )
    print('db connected')
    return conn


def diconnect(conn):
    conn.close()
    

if __name__=='__main__':
    mysqlconnection()    
