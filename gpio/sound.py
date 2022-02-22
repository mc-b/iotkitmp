import time, math, machine
from lib.config import *

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

buzzer = machine.Pin(DEFAULT_IOTKIT_BUZZER)

while True:
    try:
        p = machine.PWM(buzzer, freq=3969, duty=50 )
        time.sleep( 0.5 )
        p = machine.PWM(buzzer, freq=2800, duty=50 )    
        time.sleep( 0.5 )
    except:
        p = machine.PWM(buzzer, freq=0, duty=0 ) 
        break





