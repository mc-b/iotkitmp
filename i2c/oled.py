from machine import Pin, SoftI2C
from lib.oled.ssd1306 import SSD1306_I2C
from lib.config import *

# I2C Bus
i2c = SoftI2C(sda=Pin(DEFAULT_IOTKIT_I2C_SDA), scl=Pin(DEFAULT_IOTKIT_I2C_SCL))
display = SSD1306_I2C(128, 64, i2c)


display.text('Hey micropython!', 0, 0, 1)
display.show()



