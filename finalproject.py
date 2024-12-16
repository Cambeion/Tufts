from machine import Pin
import time
from dht import DHT11
import neopixel

NUM_LEDS = 12

leds = neopixel.NeoPixel(Pin(6), NUM_LEDS)
button = Pin(38, Pin.IN, Pin.PULL_DOWN)
sensor1 = DHT11(Pin(14))
sensor2 = DHT11(Pin(15))
heater = Pin(35, Pin.IN, Pin.PULL_DOWN)

# Initialize CSV file and write headers
with open('temperature_data.csv', 'w') as csv_file:
    csv_file.write('Time Elapsed (s),DHT11 #1 Temp (F),DHT11 #2 Temp (F)\n')

start_time = time.time()  # Track start time

while True:
    if button.value() == True: # When button is pressed for first time, start loop
        while button.value() == False: #if button is pressed again, turn off the box
            sensor2.measure()
            sensor1.measure()
            time.sleep(2)
            Cone = sensor1.temperature()
            Ctwo = sensor2.temperature()
            Ftwo = Ctwo * 9 / 5 + 32
            Fone = Cone * 9 / 5 + 32

            # Update LEDs based on temperature ranges
            if Fone < 85 or Ftwo < 85:
                for i in range(NUM_LEDS):  # Heating up, make LEDs yellow
                    leds[i] = (255, 255, 0)
                heater.on()

            if Fone > 95 or Ftwo > 95:
                for i in range(NUM_LEDS):  # Too high, make LEDs red
                    leds[i] = (255, 0, 0)
                heater.off()

            if (Fone > 85 && Fone < 95) or (Ftwo > 85 && Ftwo < 95):  # In range, LEDs are green
                for i in range(NUM_LEDS):
                    leds[i] = (0, 255, 0)
                    
            # Calculate elapsed time and log data
            elapsed_time = time.time() - start_time
            with open('temperature_data.csv', 'a') as csv_file:
                csv_file.write(f'{elapsed_time:.2f},{Fone},{Ftwo}\n')

            time.sleep(5)  # 5-second pause because your mom yells at you when you flip the heat on and off

    for i in range(NUM_LEDS):  # When off, LEDs are off
        leds[i] = (0, 0, 0)
