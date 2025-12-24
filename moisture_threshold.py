import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_soilmoisture",
    use_pure = True
)


query="select * from moisture where moisture >32"

cursor=connection.cursor()
cursor.execute(query)
moisture=cursor.fetchall()
for moist in moisture:
    print(moist)

connection.commit()
cursor.close()

