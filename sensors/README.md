Sensoren
--------
***

> [⇧ **Home**](../README.md)

![](https://raw.githubusercontent.com/iotkitv3/intro/main/images/Messysteme.png)

Quelle: Prof. Dr.-Ing. Michael Weyrich, http://wiki.zimt.uni-siegen.de/fertigungsautomatisierung

- - -

Sensoren sind technische Bauteile, die Eigenschaften der Umgebung (z. B.: Wärmestrahlung, Temperatur, Feuchtigkeit, Druck, Schall, Helligkeit oder Beschleunigung) erfassen und in ein weiter verarbeitbares elektrisches Signal umformen.

**Die nachfolgenden Sensoren sind der Vollständigkeit aufgeführt.** An dessen Stelle kommen heute, sogenannte [MEMS Sensoren](https://www.digikey.ch/de/blog/mems-sensors-are-good-but-the-revolution-is-just-beginning) zum Einsatz. Diese sind im Kapitel [I²C/TWI](../i2c/) beschrieben.


### Hall Sensor 
***

Ein [Hall Sensor](http://de.wikipedia.org/wiki/Hall-Sensor) (auch Hall-Sonde oder Hall-Geber, nach Edwin Hall) nutzt den Hall-Effekt zur Messung von Magnetfeldern.

[Hall-Effekt-Unit](https://docs.m5stack.com/en/unit/hall) integriert mit drei A3144E Hall-Sensor-Schaltern, die von integrierten Gate-Schaltungen der Serie 74HC verarbeitet werden.

Der Wert des Hall-Sensors ändert sich, wenn  der S-Pol des Magneten nahe der Oberseite des Sensors oder der N-Pol nahe der Rückseite befindet.

**Anwendungen**

*   Alarmanlagen, z.B. zum Sichern von Fenstern.
*   Im Auto zur Kontrolle ob der Sicherheitsgurt geschlossen ist, als Raddrehzahlsensoren, zur Erkennung des Zündzeitpunkts.
*   Zur Geschwindigkeitsmessung, z.B. für E-Bikes.
*   In der Kraftwerkstechnik zur Erfassung der Turbinendrehzahl.

**Beispiel**

* [read_hall.py](read_hall.py) - wie read_pot.py für den Hall (Magnet)-Sensor.
