
#pip install pymysql
import pymysql

try:
    #step1
    count = 0
    conn = pymysql.connect(host= "localhost",port=3306, user = 'root', password='rps@123')
    print(conn)
    if conn:
        print("connection established")
        #step2
        cursor = conn.cursor()  # for the navigation
        query = "select * from empdb.employee"
        #step3
        cursor.execute(query)
        #step4
        for record in cursor.fetchall():
            print(record)
            count = count + 1
        #step5
        conn.close()
except Exception as err:
    print(err)




