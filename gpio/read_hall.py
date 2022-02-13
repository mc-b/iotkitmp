from machine import Pin, ADC
from time import sleep

hall = ADC(Pin(33))
hall.atten(ADC.ATTN_11DB)       #Full range: 3.3v

while True:
  hall_value = hall.read()
  print(hall_value)
  sleep(0.1)