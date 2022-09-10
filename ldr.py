import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def ldr():
  while True:
    LIGHT_PIN = 20
    LED = 21
    GPIO.setup(LIGHT_PIN, GPIO.IN)
    GPIO.setup(LED, GPIO.OUT)
    lOld = not GPIO.input(LIGHT_PIN)
    if GPIO.input(LIGHT_PIN) != lOld:
      if GPIO.input(LIGHT_PIN):
        GPIO.output(LED, 0)
      else:
        GPIO.output(LED, 1)
      lOld = GPIO.input(LIGHT_PIN)
      time.sleep(0.2)
    return lOld
