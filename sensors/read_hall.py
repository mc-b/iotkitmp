from machine import Pin, ADC
from time import sleep
from lib.config import *

hall = ADC(Pin(DEFAULT_IOTKIT_HALL_SENSOR))
hall.atten(ADC.ATTN_11DB)       #Full range: 3.3v

while True:
  hall_value = hall.read()
  print(hall_value)
  sleep(0.1)