from machine import Pin, ADC
from time import sleep
from lib.config import *

pot = ADC(Pin(DEFAULT_IOTKIT_POTI))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

while True:
  pot_value = pot.read()
  print(pot_value)
  sleep(0.1)