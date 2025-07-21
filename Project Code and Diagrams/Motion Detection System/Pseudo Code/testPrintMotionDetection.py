from machine import Pin
import time

motion_sensor = Pin(1, Pin.IN)

time.sleep(5)

while True:
    if(motion_sensor.value()):
        print("Motion Detected")
        time.sleep(2)

