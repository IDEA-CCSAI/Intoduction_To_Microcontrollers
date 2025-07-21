# use this to download mqtt library for python (Make suer you have pip installed in system, or maybe just use an IDE like Pycharm)
# pip install paho-mqtt


import paho.mqtt.client as mqtt

BROKER = "" # mqtt broker
TOPIC = "" #make sure topic is same as sender topic

def handle_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

client = mqtt.Client()
client.connect(BROKER)
client.subscribe(TOPIC)
client.on_message = handle_message

# Simplified loop
while True:
    client.loop()
