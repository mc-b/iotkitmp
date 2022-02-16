from machine import Pin, SoftI2C
from time import sleep
from lib.config import *
import json
from lib.oled.ssd1306 import SSD1306_I2C
import usocket as socket

# Oled Display
i2c = SoftI2C(sda=Pin(DEFAULT_IOTKIT_I2C_SDA), scl=Pin(DEFAULT_IOTKIT_I2C_SCL))
display = SSD1306_I2C(128, 64, i2c)

###
# Verbindung zum Cloud Dienst
#
def getSunrise():
    s = socket.socket()

    ai = socket.getaddrinfo("api.sunrise-sunset.org", 80)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s.send(b"GET /json?lat=47.3686498&lng=8.5391825 HTTP/1.1\r\nHost: api.sunrise-sunset.org\r\n\r\n")
    rc = s.recv(4096).decode("ascii").splitlines() 
    s.close()

    for r in rc:
        if r.startswith( '{' ):
            return r
    return rc            


# Umwandlung nach JSON
rc = getSunrise()
data = json.loads( rc )
results = data['results']
sr = str(results['sunrise'])
ss = str(results['sunset'])

display.text("Sunset  " + sr, 0, 0)
display.text("Sunrise " + ss, 0, 8)
display.show()

print( sr, ss )