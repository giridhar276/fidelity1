



#pip install pymysql
import pymysql
import csv
import os
try:
    #step1
    rowcount = 0
    conn = pymysql.connect(host= "localhost",port=3306, user = 'root', password='rps@123')
    print(conn)
    if conn:
        print("connection established")
        #step2
        cursor = conn.cursor()  # for the navigation
        filename = "empinfo.csv"
        if os.path.isfile(filename):
            with open(filename) as fobj:
                reader = csv.reader(fobj)
                for line in reader:
                    workclass = line[1]
                    education = line[3]
                    query = "insert into empdb.employee values('{}','{}')".format(workclass,education)
                    cursor.execute(query)
                    rowcount = rowcount + 1
                conn.commit()
                print(rowcount,"records inserted")
        else:
            print(filename,"not found")
        conn.close()
except Exception as err:
    print(err)


