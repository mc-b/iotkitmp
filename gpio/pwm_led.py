import time, math, machine

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

led = machine.PWM(machine.Pin(33), freq=100)

for i in range(10):
    pulse(led, 20)


