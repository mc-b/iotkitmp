#####
# Boot - wird beim Reset der Device
#
# Verbindet Device mit WLAN

import network
import esp
esp.osdebug(None)
import gc
gc.collect()


# WLAN
ssid = 'LERNKUBE'
password = 'l3rnk4b3'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

### Default Pins esp32-devkitC-V4 bzw. Mapping auf IoTKitV3.1 small

DEFAULT_IOTKIT_LED1 = 26
DEFAULT_IOTKIT_BUZZER = 25

DEFAULT_IOTKIT_I2C_SCL = 4
DEFAULT_IOTKIT_I2C_SDA = 2

DEFAULT_IOTKIT_MOTOR1_FWD	= 12
DEFAULT_IOTKIT_MOTOR1_PWM	= 13
DEFAULT_IOTKIT_MOTOR1_REV	= 14
DEFAULT_IOTKIT_MOTOR2_FWD	= 16
DEFAULT_IOTKIT_MOTOR2_PWM	= 15
DEFAULT_IOTKIT_MOTOR2_REW = 17

DEFAULT_IOTKIT_SPI_MISO = 22
DEFAULT_IOTKIT_SPI_MOSI = 21
DEFAULT_IOTKIT_SPI_RST	= 18
DEFAULT_IOTKIT_SPI_SCLK = 23
DEFAULT_IOTKIT_SPI_SS   = 27

DEFAULT_IOTKIT_SERVO1	= 19
DEFAULT_IOTKIT_SERVO2 = 18

DEFAULT_IOTKIT_HALL_SENSOR = 32