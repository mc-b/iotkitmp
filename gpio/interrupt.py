from machine import Pin
from time import sleep

motion = False

def handle_interrupt(pin):
    global motion
    motion = True
    global interrupt_pin
    interrupt_pin = pin 

led = Pin(DEFAULT_IOTKIT_LED1, Pin.OUT)
pir = Pin(DEFAULT_IOTKIT_BUTTON1, Pin.IN)

pir.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

while True:
    if motion:
        print('Motion detected! Interrupt caused by:', interrupt_pin)
        led.value(1)
        sleep(2)
        led.value(0)
        print('Motion stopped!')
        motion = False 