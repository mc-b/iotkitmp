from machine import Pin, SoftI2C
from lib.config import *
from lib.oled.ssd1306 import SSD1306_I2C
import urequests
import json

# Oled Display
i2c = SoftI2C(sda=Pin(DEFAULT_IOTKIT_I2C_SDA), scl=Pin(DEFAULT_IOTKIT_I2C_SCL))
display = SSD1306_I2C(128, 64, i2c)

###
# Verbindung zum Cloud Dienst
#
req = urequests.request(method='GET', url='http://api.sunrise-sunset.org/json?lat=47.3686498&lng=8.5391825')

# Umwandlung nach JSON
rc = req.text
data = json.loads( rc )
results = data['results']
sr = str(results['sunrise'])
ss = str(results['sunset'])

display.text("Sunset  " + sr, 0, 0)
display.text("Sunrise " + ss, 0, 8)
display.show()

print( sr, ss )