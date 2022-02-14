from machine import PWM, Pin
import time

###
# Servo Ansteuerung
###
class Servo:

    # no = Servo GPIO, start = Anfangsposition (minimiert ruckeln)
    def __init__(self, no, start ):
        self.servo = PWM( Pin(no) )
        self.servo.freq(50)
        self.servo.duty(start)

    # Position von 20 - 150 setzen
    def set(self, pos):
        self.servo.duty(pos)

    # PWM freigeben
    def deinit(self):
        self.servo.deinit()        
