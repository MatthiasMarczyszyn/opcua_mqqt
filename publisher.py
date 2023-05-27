import paho.mqtt.client as mqtt
import time

mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_client = mqtt.Client("Temperature_in_Warehouse")
mqtt_client.connect(mqtt_broker)

while True:
    
    mqtt_client.publish("Temp1", 1000)
    time.sleep(1)
