import time
import network
from umqtt.simple import MQTTClient
import urequests
from machine import Pin


motion_sensor = Pin(1, Pin.IN)

#wifi connection
wifi = ''
wifi_password = ''


#mqtt connection
brooker = "" 
client_id = "" #Use any unique id
topic = "" #Please ensure your receving end has same topic
message = "motion"


#Phone notifcation Tokens
user_token = ""
api_token =  "" 


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    wlan.disconnect()
    time.sleep(0.5)

    if not wlan.isconnected():
        print("connecting to wifi")
        wlan.config(txpower=8.5)  
        wlan.connect(wifi, wifi_password)
        
        while not wlan.isconnected():
            time.sleep(1)
            print(".", end="")
        
        print("Connected to wifi")
        
        
        

def send_mqtt_signal():
    print("attempting to send mqtt signal")

    try:
        client = MQTTClient(client_id, brooker, port=1883)
        client.connect()
        print("Connected to broker")
        client.publish(topic, message)
        print("send msg sucessfully")
    except Exception as e:
        print("Error sending signal: ", e)
    finally:
        client.disconnect()

def send_phone_notification():
    try:
        print("Sending phone notification...")
        url = "https://api.pushover.net/1/messages.json"
        data = (
            "token=" + api_token +
            "&user=" + user_token +
            "&message=" + "🚨 Motion detected from ESP32!"
        )
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = urequests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            print("Notification sent successfully!")
        else:
            print("Notification failed:", response.status_code)
            print(response.text) 
    except Exception as e:
        print("Notification Error:", e)
    finally:
        response.close()








time.sleep(5)

while True:
    if(motion_sensor.value()):
        print("Motion Detected")
        connect_wifi()
        send_mqtt_signal()
        send_phone_notification()
        time.sleep(2)





