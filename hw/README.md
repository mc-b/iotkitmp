ESP32-DevKitC
-------------

![](images/esp32-devkitC-v4-pinout.png)

- - -


* 32-Bit-MCU und 2,4-GHz-WLAN und Bluetooth/Bluetooth LE
* Eingebetteter ESP32, zwei oder ein Xtensa® 32-Bit-LX6-Mikroprozessor(en) mit einstellbarer Taktfrequenz von 80 MHz bis 240 MHz
* +19,5 dBm Ausgangsleistung sorgen für eine gute physikalische Reichweite
* Klassisches Bluetooth für Legacy-Verbindungen, unterstützt auch L2CAP, SDP, GAP, SMP, AVDTP, AVCTP, A2DP (SNK) und AVRCP (CT)
* Unterstützung für Bluetooth Low Energy (Bluetooth LE)-Profile einschließlich L2CAP, GAP, GATT, SMP und GATT-basierte Profile wie BluFi, SPP-like usw
* Bluetooth Low Energy (Bluetooth LE) stellt eine Verbindung zu Smartphones her und sendet Niedrigenergie-Beacons zur einfachen Erkennung
* Der Ruhestrom beträgt weniger als 5 μA und eignet sich daher für batteriebetriebene und tragbare Elektronikanwendungen
* Zu den Peripheriegeräten gehören kapazitive Berührungssensoren, Hall-Sensor, SD-Kartenschnittstelle, Ethernet, Hochgeschwindigkeits-SPI, UART, I2S und I2C
* Vollständig zertifiziert mit integrierter Antenne und Software-Stacks

### Pins

* 22 Pins In/Out
*  4 Pins nur Input
* max. 8 PWM Channels

### Firmware Update

    esptool.py --chip esp32 --port COM13 erase_flash
    esptool.py --chip esp32 --port COM13 --baud 460800 write_flash -z 0x1000 hw/firmware/esp32-idf3-20210202-v1.14.bin

### Links

* [Hersteller](https://www.espressif.com/en/products/modules)
* [Board](https://www.mouser.ch/ProductDetail/356-ESP32-DEVKTC32VE)
* [Firmware](https://micropython.org/download/esp32/) - Version V1.14 verwenden, V1.18 funktioniert PWM nicht.

