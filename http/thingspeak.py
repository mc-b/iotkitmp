from machine import I2C, Pin, SoftI2C
from lib.sensors.bmp180 import BMP180
from time import sleep
from lib.config import *
from lib.oled.ssd1306 import SSD1306_I2C
import urequests

# 
i2c = SoftI2C(sda=Pin(DEFAULT_IOTKIT_I2C_SDA), scl=Pin(DEFAULT_IOTKIT_I2C_SCL))
display = SSD1306_I2C(128, 64, i2c)

bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

while True:
  temp = bmp180.temperature
  pres = bmp180.pressure
  values = "key=" + "A2ABBMDJYRAMA6JM" + "&field1=" + str(temp) + "&field2=" + str(pres / 1000)

  display.text("Temp: " + str(temp), 0, 0)
  display.text("Pres: " + str(pres / 1000), 0, 8)
  display.show()
  print ( values )

  try:
    req = urequests.request(method='POST', url='http://api.thingspeak.com/update?' + values)
  except:
    print( 'failed')

  sleep( 15 )
  
