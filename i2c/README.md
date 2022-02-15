## I²C/TWI (Inter-Integrated Circuit, bzw. Two-Wire-Interface)
***

> [⇧ **Home**](../README.md)

![](https://raw.githubusercontent.com/iotkitv3/intro/main/images/I2C.png) 

[I²C-Bus mit einem Master und drei Slaves](http://de.wikipedia.org/wiki/I%C2%B2C)

- - -

I²C, für englisch Inter-Integrated Circuit, im Deutschen gesprochen als I-Quadrat-C oder englisch I-Squared-C oder I-2-C, ist ein von Philips Semiconductors (heute NXP Semiconductors) entwickelter serieller Datenbus.

Der Bus wurde 1982 von Philips eingeführt zur Geräte internen Kommunikation zwischen ICs in z.B. CD-Spielern und Fernsehgeräten.

I²C ist als **Master-Slave-Bus** konzipiert. Ein Datentransfer wird immer durch einen Master (die MCU auf dem Board) initiiert; der über eine Adresse angesprochene Slave (die Sensoren auf dem Board) reagiert darauf. Mehrere Master sind möglich (Multimaster-Mode). Im Multimaster-Mode können zwei Master-Geräte direkt miteinander kommunizieren, dabei arbeitet ein Gerät als Slave.

Der **Bustakt** wird immer vom Master ausgegeben. Für die verschiedenen Modi ist jeweils ein maximal erlaubter Bustakt vorgegeben. In der Regel können aber auch beliebig langsamere Taktraten verwendet werden, falls diese vom Master-Interface unterstützt werden. Bestimmte ICs (z.B. Analog-Digital-Umsetzer) benötigen jedoch eine bestimmte, minimale Taktfrequenz, um ordnungsgemäss zu funktionieren.

Eine **Standard-I²C-Adresse ist das erste vom Master gesendete Byte**, wobei die ersten sieben Bit die eigentliche Adresse darstellen und das achte Bit (R/W-Bit) dem Slave mitteilt, ob er Daten vom Master empfangen soll (LOW), oder Daten an den Master zu übertragen hat (HIGH). I²C nutzt daher einen Adressraum von 7 Bit, was bis zu **112 Knoten auf einem Bus** erlaubt (16 der 128 möglichen Adressen sind für Sonderzwecke reserviert).

Das Protokoll des I²C-Bus ist von der Definition her recht einfach, aber physikalisch auch recht störanfällig. Auch ist er **ungeeignet zur Überbrückung größerer Entfernungen**. Der Bus kann jedoch mit speziellen Treibern auf ein höheres Strom- und/oder Spannungslevel umgesetzt werden, wodurch der Störabstand und die mögliche Leitungslänge steigen.

Der Bus braucht zur Terminierung zwei Widerstände von ca. 2.2K - 4.7K Ohm (je nach Länge der Kabel, siehe 6-Achsen-Sensor) und alle Geräte müssen an der gleichen Ground Leitung angeschlossen sein.

**Die I2C Sensoren und Aktoren auf dem Board sind anhand der Hexadecimalen Nummer, z.B. 0x78 neben dem OLED Display, zu erkennen.**

### Anwendungen 

*   Ansprechen von Peripherie Bausteinen wie Temperatursensor, [3-axis Beschleunigungsmesser (Accelerometer) and Magnetfeldstärkenmessgerät (Magnetometer)](http://developer.mbed.org/users/JimCarver/code/FXOS8700Q/)
*   Ansprechen von Analog/Digital and Digital/Analog IC&#039;s, z.B. [PCF8591](http://developer.mbed.org/users/wim/notebook/pcf8591-i2c-4-channel-8-bit-ad-and-1-channel-8-bit/)
*   Verbinden von Boards, auch über grössere Distanzen. Siehe [www.mikrokontroller.net](http://www.mikrocontroller.net/articles/I%C2%B2C) und [RocNet](http://wiki.rocrail.net/doku.php?id=rocnet:rocnet-prot-de)

## Beispiele

* [show_devices.py](show_devices.py) - Ausgabe der I2C Geräte
* [BMP180](#bmp180)
* [APDS-9960](#APDS-9960)
* [oled.py](oled.py) - Ansteuerung des OLED Displays


## BMP180
***

Der BMP180 Präzisionssensor von Bosch ist die beste kostengünstige (~60cent) Messlösung zur Messung von Luftdruck und Temperatur.

Der BMP180 liefert Temperatur und Luftdruck zurück.

Für Details siehe [Datenblatt](https://www.mouser.ch/datasheet/2/783/BST-BMP180-DS000-1509579.pdf).

### Anwendungen 

* Überwachung von Temperatur und Luftdruck
* Kann auch als Höhenmesser verwendet werden


**Beispiel(e)**

* [temp.py](temp.py) - Ausgabe von Temperatur, Luftdruck und Höhe.


## APDS-9960
***

Der APDS-9960 ist ein RGB- und Gestensensor, der Umgebungslicht- und Farbmessung, Näherungserkennung und berührungslose Gestenerkennung bietet. 

Mit diesem RGB- und Gestensensor können Sie einen Computer, einen Mikrocontroller, einen Roboter und mehr mit einem einfachen Handgriff steuern! 

Dies ist derselbe Sensor, den das Samsung Galaxy S5 verwendet, und wahrscheinlich einer der besten Gestensensoren auf dem Markt für den Preis.

### Anwendungen 

* Erfassung des Menschlichen Auges via Smartphone
* Erkennung von [Gesten](https://www.youtube.com/watch?v=A3QRyixnEl8).

**Beispiel(e)**

* [ambient.py](ambient.py) - Lichtstärke
* [gesture.py](gesture.py) - Bewegungen. Dazu die Hand von allen Richtungen über den Sensor bewegen.
* [prox.py](prox.py) - Abstandsmesser. Dazu die Hand auf und ab über dem Sensor bewegen.


### Links

* [APDS-9960 Datenblatt](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/1/Avago-APDS-9960-datasheet.pdf)
* [APDS-9960 RGB and Gesture Sensor Hookup Guide](https://learn.sparkfun.com/tutorials/apds-9960-rgb-and-gesture-sensor-hookup-guide)
* [Produktseite](https://www.sparkfun.com/products/12787)
