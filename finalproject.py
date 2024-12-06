from machine import Pin
import time
from dht import DHT11

button = Pin(37, Pin.IN, Pin.PULL_DOWN)
sensor1 = DHT11(Pin(23))
sensor2 = DHT11(Pin(24))
sensor3 = DHT11(Pin(25))
sensor4 = DHT11(Pin(26)) #top of box

LED = Pin(35, Pin.IN, Pin.PULL_DOWN)

while True:
    while(button == True):
        sensor4.measure()
        C = sensor4.temperature()
        F = C * 9/5 + 32
        if(F < 85):
            LED.off()
            #turn on heater
        if(F > 95):
            LED.off()
            #turn off heater
        if(F < 95 && F > 85):
            LED.on()
        time.sleep(5)
    LED.off()
