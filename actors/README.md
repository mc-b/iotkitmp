Aktoren
-------
***

> [⇧ **Home**](../README.md)


Aktoren (Wandler; Antriebselemente) setzen die elektronischen Signale in mechanische Bewegung oder andere physikalische Grössen um und greifen damit aktiv in die Umgebung des eingebetteten Systems ein.

### Beispiele

* [DC Motor](#gleichstrom-motor) 
* [Servo](#servo) 
* [Schrittmotor](#schrittmotor)

### Gleichstrom Motor
***

> [⇧ **Nach oben**](#beispiele)

![](https://raw.githubusercontent.com/iotkitv3/intro/main/images/actors/Motor.png) 

[Motoren](http://de.wikipedia.org/wiki/Elektromotor)

- - -

Elektromotor bezeichnet einen elektromechanischen Wandler (elektrische Maschine), der elektrische Energie in mechanische Energie umwandelt. In herkömmlichen Elektromotoren wird die Kraft, die von einem Magnetfeld auf die stromdurchflossenen Leiter einer Spule ausgeübt wird, in Bewegung umgesetzt.

**Anwendungen** 

*   Antrieb von Bahnen, Elektrokarren, Gabelstabel, Funkgesteuerte Modellautos (RC-Car), Robotern etc.

**Beispiel**

* [dc_motor.py](dc_motor.py) - bewegt den Motor an Anschluss `m01` auf dem IoTKitV3 Shield.

### Servo 
***

> [⇧ **Nach oben**](#beispiele)

![](https://raw.githubusercontent.com/iotkitv3/intro/main/images/actors/ServoOpen.png) ![](https://raw.githubusercontent.com/iotkitv3/intro/main/images/actors/ServoSignal.png)

[http://wiki.rc-network.de/Servo](http://wiki.rc-network.de/Servo)

- - -

Der Servo (auch Rudermaschine) hat die Aufgabe, entsprechend dem Signal, dass er vom Empfänger erhält, die Ruder (oder andere Komponenten am Modell) zu stellen.

Servo lassen sich, in der Regel, von 0 - 180° bewegen. Der entsprechende Stellwinkel wird mittels eines Wert von 0.0 bis 1.0 angegeben.

Es gibt analoge und digitale Servos. Der Unterschied liegt darin, dass digitale Servo erst anfangen den Stellwinkel zu wechseln, wenn ein sauberes Signal anliegt.

Weitere Informationen und eine Ausführliche Einführung in Englisch [An Introduction to RC Servos](http://developer.mbed.org/users/4180_1/notebook/an-introduction-to-servos/)

**Anwendungen** 

*   Steuerung von Roboterarmen
*   Modellflugzeuge
*   Schalten von Weichen auf der Modelleisenbahn

**Beispiel**

* [servos.py](servos.py) - steuert zwei Servos auf dem IoTKitV3 Shield an den Anschlüssen `D8` und `D9`. Das orange Kabel kommt auf den `S` Pin.


### Schrittmotor
***

> [⇧ **Nach oben**](#beispiele)

Ein Schrittmotor ist ein Synchronmotor, bei dem der Rotor (drehbares Motorteil mit Welle) durch ein gesteuertes, schrittweise rotierendes, elektromagnetisches Feld der Statorspulen (nicht drehbarer Motorteil) um einen minimalen Winkel (Schritt) oder sein Vielfaches gedreht werden kann.

Ein Schrittmotor hat eine fixe Schrittanzahl pro Umdrehung. 

Zur erstmaligen Positionierung wird, in der Regel, ein Endstop Schalter verwendet. [CNC Maschinen](http://de.wikipedia.org/wiki/CNC-Maschine) besitzen zusätzlich, wegen der Verletzungsgefahr einen Notstopp Schalter mit Einrastfunktion.

**Anwendungen** 

*   Typische Anwendungsgebiete sind Drucker oder der Antrieb des Schreib-/Lesekopfes in einem CDROM Laufwerken. Aufgrund ihrer hohen Genauigkeit werden sie auch in computergesteuerten Werkzeugmaschinen zur Positionierung der Werkzeuge verwendet. Durch die ständig sinkenden Kosten für die Ansteuerelektronik werden sie auch zunehmend im Konsumgüterbereich verwendet. So sind in Kraftfahrzeugen der mittleren und gehobenen Kategorie heute bis über 50 Schrittmotoren im Einsatz, die Betätigung der vielen Klappen einer automatischen Heizungs- und Klimaanlage ist dafür ein Beispiel.

**Beispiel**

* folgt.

