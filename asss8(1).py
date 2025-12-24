import paho.mqtt.client as mqtt
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_home"
)
cursor = db.cursor()

def on_message(client, userdata, message):
    topic = message.topic
    value = float(message.payload.decode())

    if topic == "sensor/ldr":
        sensor_type = "ldr"
        print("LDR data stored:", value)

    elif topic == "sensor/lm35":
        sensor_type = "lm35"
        print("LM35 data stored:", value)

    query = "INSERT INTO sensor_data (sensor_type, value) VALUES (%s, %s)"
    cursor.execute(query, (sensor_type, value))
    db.commit()

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_message = on_message

subscriber.connect("localhost", 1883)
subscriber.subscribe("sensor/ldr")
subscriber.subscribe("sensor/lm35")

subscriber.loop_forever()
