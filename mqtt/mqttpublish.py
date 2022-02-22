####
# Test der MQTT Library

import time
from machine import I2C, Pin, SoftI2C
from lib.sensors.bmp180 import BMP180
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

# Klassifikation 
cls       = ( "low", "middle", "high" )
type      = 0

bus = SoftI2C(sda=Pin(DEFAULT_IOTKIT_I2C_SDA), scl=Pin(DEFAULT_IOTKIT_I2C_SCL))

bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325


def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

def connect_and_subscribe():
  global client_id, mqtt_server, topicSERVO
  client = MQTTClient(client_id, hostname)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topicSERVO)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (hostname, topicSERVO))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()


while True:
  try:
    client.check_msg()
    msg = "0x3c," + str(bmp180.temperature) + "," + str(bmp180.pressure / 1000)
    client.publish(topicTEMP, msg)
    print( topicTEMP, msg )
    time.sleep( 1.0 )
  except OSError as e:
    restart_and_reconnect()