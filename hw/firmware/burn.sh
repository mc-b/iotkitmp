#!/bin/bash

COM=$(powershell '[System.IO.Ports.SerialPort]::getportnames()')

esptool.py --chip esp32 --port $COM erase_flash
esptool.py --chip esp32 --port $COM --baud 460800 write_flash -z 0x1000 esp32-idf3-20210202-v1.14.bin
