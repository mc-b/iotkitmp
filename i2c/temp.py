from machine import I2C, Pin, SoftI2C
from lib.sensors.bmp180 import BMP180

bus = SoftI2C(sda=Pin(DEFAULT_IOTKIT_I2C_SDA), scl=Pin(DEFAULT_IOTKIT_I2C_SCL))

bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

temp = bmp180.temperature
p = bmp180.pressure
altitude = bmp180.altitude
print(temp, p, altitude)
