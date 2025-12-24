import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="SA11@kbksb",
    database="iot_etc",
    use_pure=True
)

roll_no=int(input("enter the rollno you want to delete: "))

query=f"delete from students where roll_no={roll_no};"

cursor=connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()