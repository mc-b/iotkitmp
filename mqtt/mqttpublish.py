####
# MQTT Publish 
#
# Wertet Temperatur Sensor, Button und RFID Reader aus und sendet die Daten an MQTT Broker
 
import time
from machine import I2C, Pin, SoftI2C, SoftSPI
from lib.sensors.bmp180 import BMP180
from lib.sensors.mfrc522 import MFRC522
from lib.config import *
from umqtt.robust import MQTTClient
import ubinascii
import machine
from lib.config import *
import micropython
import network

client_id = ubinascii.hexlify(machine.unique_id())

# Topic's
topicTEMP   = b"iotkit/sensor"
topicALERT  = b"iotkit/alert"
topicRFID   = b"iotkit/rfid"
topicSERVO  = b"iotkit/servo"
# MQTT Brocker
hostname    = "cloud.tbz.ch"
port        = 1883

# Klassifikation 
cls       = ( "low", "middle", "high" )
type      = 0

# Temperatur Sensor
bus = SoftI2C(sda=Pin(DEFAULT_IOTKIT_I2C_SDA), scl=Pin(DEFAULT_IOTKIT_I2C_SCL))

bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

# RFID Reader
sck = Pin(DEFAULT_IOTKIT_SPI_SCLK)
mosi = Pin(DEFAULT_IOTKIT_SPI_MOSI)
miso = Pin(DEFAULT_IOTKIT_SPI_MISO)
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
sda = Pin(DEFAULT_IOTKIT_SPI_SS, Pin.OUT)
rdr = MFRC522(spi, sda)

# Button
button = Pin(DEFAULT_IOTKIT_BUTTON1, Pin.IN)

# MQTT Subscribe
def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

# MQTT Login
def connect_and_subscribe():
  global client_id, hostname, port, topicSERVO
  client = MQTTClient(client_id, hostname, port)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topicSERVO)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (hostname, topicSERVO))
  return client

# MQTT Restart 
def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()


### Hauptprogramm

counter = 1

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()


while True:
  try:
    client.check_msg()

    # Temperatur
    if counter % 3 == 1:
        msg = "0xBC," + str(bmp180.temperature - 5) + "," + str(bmp180.pressure / 1000) + ",low"
    if counter % 3 == 2:
        msg = "0xBC," + str(bmp180.temperature) + "," + str(bmp180.pressure / 1000) +  ",middle"
    if counter % 3 == 0:
        msg = "0xBC," + str(bmp180.temperature + 5) + "," + str(bmp180.pressure / 1000) + ",high"
    client.publish(topicTEMP, msg)
    print( topicTEMP, counter, msg )
    counter = counter + 1

    # Button startet BPMN Prozess
    if  button.value() == 0:
        client.publish(topicALERT, "alert")
        print( topicALERT, counter, "alert" )

    uid = ""
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            client.publish(topicRFID, uid )
            print(topicRFID, counter, uid)

    time.sleep( 1.0 )
  except OSError as e:
    restart_and_reconnect()