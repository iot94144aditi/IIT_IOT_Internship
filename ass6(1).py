import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)


id=int(input("enter id: "))
temprature=float(input("enter temprature: "))
humidity=float(input("enter humidity: "))
timestamp=(input("enter timestamp: "))

query=f"insert into sensor_readings values('{id}','{temprature}','{humidity}','{timestamp}')"

cursor=connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()

