import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def dht_22():
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 2
    GPIO.setup(DHT_PIN, GPIO.IN)
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            temp = '{0:0.1f}'.format(temperature, humidity)
            humi = '{1:0.1f}'.format(temperature, humidity)
        else:
            print("Failed to retrieve data from humidity sensor")
        time.sleep(0.5)
    return humidity, temperature

