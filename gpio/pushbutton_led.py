
from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)
button = Pin(0, Pin.IN)

while True:
  led.value(button.value())
  print( button.value() )
  sleep(0.5)
