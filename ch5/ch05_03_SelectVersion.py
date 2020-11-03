import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    db='investar',
    user='root',
    passwd='1234',
    autocommit=True
)

cursor = conn.cursor()
cursor.execute("SELECT VERSION();")
result = cursor.fetchone()

print("Mysql version : {}".format(result))

conn.close()
