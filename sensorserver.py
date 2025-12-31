from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="iot_db"
)
cursor = db.cursor(dictionary=True)

# CREATE
@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    cursor.execute(
        "INSERT INTO sensor_readings (temperature, humidity, timestamp) VALUES (%s,%s,%s)",
        (data['temperature'], data['humidity'], datetime.now())
    )
    db.commit()
    return "Record inserted"

# READ ALL
@app.route('/read', methods=['GET'])
def read_data():
    cursor.execute("SELECT * FROM sensor_readings")
    return jsonify(cursor.fetchall())

# UPDATE
@app.route('/update/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.json
    cursor.execute(
        "UPDATE sensor_readings SET temperature=%s, humidity=%s WHERE id=%s",
        (data['temperature'], data['humidity'], id)
    )
    db.commit()
    return "Record updated"

# DELETE
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_data(id):
    cursor.execute("DELETE FROM sensor_readings WHERE id=%s", (id,))
    db.commit()
    return "Record deleted"

# THRESHOLD
@app.route('/threshold/<float:value>', methods=['GET'])
def threshold(value):
    cursor.execute("SELECT * FROM sensor_readings WHERE temperature < %s", (value,))
    return jsonify(cursor.fetchall())

if __name__ == '__main__':
    app.run()
