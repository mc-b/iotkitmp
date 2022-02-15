GPIO
----
***

> [⇧ **Home**](../README.md)


![](../images/esp32-devkitC-v4-pinout.png)

- - -

Allzweckeingabe/-ausgabe (engl. GPIO - General Purpose Input/Output) ist ein allgemeiner Kontaktstift (Pin) an einem Mikrocontroller, dessen Verhalten, unabhängig, ob als Eingabe- oder Ausgabekontakt, durch logische Programmierung frei bestimmbar ist. GPIO-Kontakten ist kein Zweck vorgegeben, sie sind daher standardmäßig unbelegt.

Die Boards, bzw. Micropython verfügt u.a. über die nachfolgenden Funktionen um GPIOs direkt anzusteuern.

### Pin 

Dient dazu um den digitalen Wert eines Pins Ein/Aus zu setzen. 

Oder einen digitalen Wert (0 oder 1) eines Pins abzufragen.

* [Dokumentation](https://docs.micropython.org/en/latest/library/machine.Pin.html)

**Beispiele**

* [pushbutton_led.py](pushbutton_led.py) - bringt die LED zum leuchten, wenn der `Boot` Button gedrückt wird.
* [interrupt.py](interrupt.py) - wie pusbutton aber mittels Interrupts gesteuert.

**Anwendungen Output** 

*   Ansteuerung von LEDs, z.B. für Taschenlampe, [Kultpfunzel](http://kultpfunzel.ch/) , [Fernsehsimulator,](http://www.pearl.ch/ch-a-NC5312-3110.shtml) [Kleidung](http://www.get-a-led.de/led-t-shirts/led-kleidung-stereo-mc/), Statusanzeigen etc.
*   2 DigitalOut für die Richtungsbestimmung bei Motoren
*   4 DigitalOut für die Ansteuerung von Schrittmotoren

**Anwendungen Input** 

*   Externer Feedback, z.B. Taster.
*   Sensoren welche bei Eintreten eines Ereignisses zwischen 0 und 1 umschalten, z.B. Bewegungsmelder


### PWM

[Pulsweitenmodulation](http://de.wikipedia.org/wiki/Pulsweitenmodulation) (kurz PWM), ist eine Modulationsart, bei der die elektrische Spannung zwischen Ground (0 Volt) und 3.3 Volt wechselt.

Die relative Länge des Pulses wird Tastgrad (englisch duty cycle) genannt.

Der Abstand zwischen dem Startpunkt zwei aufeinanderfolgender Pulse wird "Periode" genannt.

* [Dokumentation](https://docs.micropython.org/en/latest/library/machine.PWM.html)

**Beispiele**

* [pwm_led.py](pwm_led.py) - lässt die LED aufleuchten
* [sound.py](sound.py) - spielt Musik auf dem Buzzer.

**Anwendungen** 

*   Licht dimmen
*   Motoren Geschwindigkeit regeln
*   Töne erzeugen

### ADC

Ein Analogsignal ist ein Signals mit stufenlosem und unterbrechungsfreiem Verlauf

In der Elektronik erfolgt die Umsetzung eines elektrischen Analogsignals in ein nutzbares Digitalsignal mittels Analog-Digital-Umsetzern (ADU), die umgekehrte Richtung erfolgt mittels Digital-Analog-Umsetzern (DAU).

* [Dokumentation](https://docs.micropython.org/en/latest/library/machine.ADC.html)

**Beispiele**

* [read_pot.py](read_pot.py) - liest den Wert des Potentimeters auf dem IoTKitV3 Shield und gibt diesen in der Console aus.
* [read_hall.py](read_hall.py) - wie read_pot.py für den Hall (Magnet)-Sensor.

**Anwendungen**

*   Auslesen eines Sensorwertes, z.B. Lichtintensität
*   Zusammen mit einen [Potentiometer](http://de.wikipedia.org/wiki/Potentiometer) um einen Schwellenwert für ein Ereignis, z.B. für das Anschalten des Lichtes, oder um die Geschwindigkeit für einen Motor einzustellen.





