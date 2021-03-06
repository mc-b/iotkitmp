from machine import Pin, PWM
import time 
from lib.actors.servo import Servo
from lib.config import *

PAUSE = 0.01

# Servo Pins
pins = ( DEFAULT_IOTKIT_SERVO1, DEFAULT_IOTKIT_SERVO2 )
servos = []

try:
    for pin in pins:
        servos.append( Servo(pin, 20) )

    for duty in range(20, 80):
        for servo in servos:
          servo.set(duty)
          time.sleep(PAUSE) 
    time.sleep( 1.0 )          

    for duty in range(80, 20, -1):
        for servo in servos:
          servo.set(duty)
          time.sleep(PAUSE)


finally:
    for servo in servos:
        try:
            servo.deinit()
        except:
            pass