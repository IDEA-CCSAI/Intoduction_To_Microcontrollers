# use this to download mqtt library for python (Make suer you have pip installed in system, or maybe just use an IDE like Pycharm)
# pip install paho-mqtt

import paho.mqtt.client as mqtt

BROKER = "" # mqtt broker
TOPIC = "" #make sure topic is same as receiver topic

# Create a client and connect
client = mqtt.Client()
client.connect(BROKER, 1883, 60)

# Publish a test message
client.publish(TOPIC, "hello from PC")

# Disconnect after sending
client.disconnect()

print("Message sent.")
