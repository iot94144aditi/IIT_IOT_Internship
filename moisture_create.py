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


sensor_id=int(input("enter sensor_id: "))
moisture=float(input("enter temprature: "))
DateAndTime=datetime.datetime.now()


query=f"insert into moisture values('{sensor_id}','{moisture}','{DateAndTime}')"

cursor=connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()

