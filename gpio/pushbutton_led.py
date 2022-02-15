
from machine import Pin
from time import sleep
from lib.config import *

led = Pin(DEFAULT_IOTKIT_LED1, Pin.OUT)
button = Pin(DEFAULT_IOTKIT_BUTTON1, Pin.IN)

while True:
  led.value(button.value())
  print( button.value() )
  sleep(0.5)
