from time import sleep_ms
from machine import Pin, SoftSPI
from lib.config import *
from lib.sensors.mfrc522 import MFRC522

sck = Pin(DEFAULT_IOTKIT_SPI_SCLK, Pin.OUT)
mosi = Pin(DEFAULT_IOTKIT_SPI_MOSI, Pin.OUT)
miso = Pin(DEFAULT_IOTKIT_SPI_MISO, Pin.OUT)
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
sda = Pin(DEFAULT_IOTKIT_SPI_SS, Pin.OUT)

print ( "RFID Test" )

def do_read():
    try:
        while True:
            rdr = MFRC522(spi, sda)
            uid = ""
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK:
                    uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print(uid)
                    sleep_ms(100)
    except KeyboardInterrupt:
        print("Bye")

do_read()
