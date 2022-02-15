from time import sleep

from machine import Pin, I2C
from lib.config import *

from lib.sensors.apds9960 import *
from lib.sensors.apds9960 import uAPDS9960 as APDS9960

bus = I2C(sda=Pin(DEFAULT_IOTKIT_I2C_SDA), scl=Pin(DEFAULT_IOTKIT_I2C_SCL))

apds = APDS9960(bus)

print("Light Sensor Test")
print("=================")
apds.enableLightSensor()

oval = -1
while True:
    sleep(0.25)
    val = apds.readAmbientLight()
    if val != oval:
        print("AmbientLight={}".format(val))
        oval = val

