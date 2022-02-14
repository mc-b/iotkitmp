from lib.actors.dcmotor import DCMotor
from machine import Pin, PWM
from time import sleep

frequency = 15000

pin1 = Pin(DEFAULT_IOTKIT_MOTOR1_FWD, Pin.OUT)
pin2 = Pin(DEFAULT_IOTKIT_MOTOR1_REV, Pin.OUT)
enable = PWM(Pin(DEFAULT_IOTKIT_MOTOR1_PWM), frequency)

dc_motor = DCMotor(pin1, pin2, enable)

dc_motor.forward(50)
sleep(2)
dc_motor.stop()
sleep(1)
dc_motor.backwards(100)
sleep(2)
dc_motor.forward(25)
sleep(5)
dc_motor.stop()
