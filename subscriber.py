import paho.mqtt.client as mqtt
import time




def on_messege(client,userdata,message):
    print(f"Recive {message.payload.decode('utf-8')}")


mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_client = mqtt.Client("Server")
mqtt_client.connect(mqtt_broker)

mqtt_client.loop_start()
mqtt_client.subscribe("Temp1")
mqtt_client.on_message = on_messege
time.sleep(4)
mqtt_client.loop_stop()

