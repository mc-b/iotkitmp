## UART (Universal Asynchronous Receiver Transmitter)
***

> [⇧ **Home**](../README.md)

![](../images/UART.png)

Das untere Diagramm zeigt die dazu invertierten Spannungspegel auf der RS-232-Schnittstelle. [Quelle Wikipedia](http://de.wikipedia.org/wiki/Universal_Asynchronous_Receiver_Transmitter)

- - - 

Universal Asynchronous Receiver Transmitter, kurz UART, ist eine elektronische Schaltung, die zur Realisierung digitaler serieller Schnittstellen dient. Dabei kann es sich sowohl um ein eigenständiges elektronisches Bauelement (ein UART-Chip bzw. -Baustein) oder um einen Funktionsblock eines höherintegrierten Bauteils (z. B. eines Mikrocontrollers) handeln.

Eine UART-Schnittstelle dient zum Senden und Empfangen von Daten über eine Datenleitung und bildet den Standard der seriellen Schnittstellen an PCs und Mikrocontrollern. Auch im industriellen Bereich ist die Schnittstelle mit verschiedenen Interfaces (z. B. [RS-232](http://de.wikipedia.org/wiki/RS-232) oder [EIA-485](http://de.wikipedia.org/wiki/EIA-485)) sehr verbreitet.

Die Daten werden als serieller digitaler Datenstrom mit einem fixen Rahmen übertragen, der aus einem Start-Bit, fünf bis maximal neun Datenbits, einem optionalen Parity-Bit zur Erkennung von Übertragungsfehlern und einem Stopp-Bit besteht. Um dem Empfänger eine Synchronisationszeit auf den Takt der empfangenen Daten einzuräumen, kann das Stopp-Bit auf das 1,5 oder 2-fache der normalen Übertragungszeit eines Bits verlängert werden. Das wird als 1,5 bzw. 2 Stopp-Bits bezeichnet.

**In einfachen Mikrocontroller-Systemen werden Daten häufig über UART-Schnittstellen ausgetauscht, die ohne Handshake, nur über Rx und Tx, verwirklicht sind. Diese für kurze Entfernungen geeignete, auch [CMOS-UART bzw. TTL-UART](http://de.wikipedia.org/wiki/Logikpegel) genannte Implementierung wird von praktisch allen Mikrocontrollern unterstützt und kann bei entsprechend geringen Übertragungsraten auch über Software realisiert werden.**

Das ESP32 Board stellt ein Serielle Schnittstelle auf mittels USB Bus zur Verfügung. 

Zusätzlich sind die Pins `GPIO1 und GPIO3` auf den IoTKitV3 Shield nach `D0 und D1` geführt.

**Anwendungen** 

* Ausgabe von Debug Informationen
* Fernsteuerung des Gerätes z.B. wie bei 3D Druckern
* Board - PC Kommunikation

