from machine import Pin
import time
from dht import DHT11

button = Pin(38, Pin.IN, Pin.PULL_DOWN)
sensor1 = DHT11(Pin(15))
red = Pin(2, Pin.OUT)
yellow = Pin(4, Pin.OUT)
green = Pin(3, Pin.OUT)


# Initialize CSV file and write headers
with open('temperature_data1.csv', 'w') as csv_file:
    csv_file.write('Time Elapsed (s),DHT11 #1 Temp (F)\n')

start_time = time.time()  # Track start time


while True:
    sensor1.measure()
    time.sleep(2)
    Cone = sensor1.temperature()
    Fone = Cone * 9 / 5 + 32
    print(Fone)
    green.off()
    yellow.off()
    red.off()
    
    # Update LEDs based on temperature ranges
    if Fone < 85:
        print("heating up \n")
        yellow.on()

    if Fone > 95:
        print("too high \n")
        red.on()

    if Fone > 85 and Fone < 95:  # In range, LEDs are green
        print("in range \n")
        green.on()
                    
            # Calculate elapsed time and log data
    elapsed_time = time.time() - start_time
    with open('temperature_data.csv', 'w') as csv_file:
        csv_file.write(f'{elapsed_time:.2f},{Fone}\n')

    time.sleep(5)  # 5-second pause because your mom yells at you when you flip the heat on and off

