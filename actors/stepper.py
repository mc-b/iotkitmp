### Schrittmotor an MCP23017 I2C I/O

from machine import Pin, SoftI2C
import time
from lib.io.mcp23017 import MCP23017
from lib.oled.ssd1306 import SSD1306_I2C
from lib.config import *

i2c = SoftI2C(sda=Pin(DEFAULT_IOTKIT_I2C_SDA), scl=Pin(DEFAULT_IOTKIT_I2C_SCL))

display = SSD1306_I2C(128, 64, i2c)

display.text('Stepper Test!', 0, 0, 1)
display.show()

# Stepper 1: 8 - 11, Stepper 2: 12 - 15, Stepper 3: 4 - 7, Endschalter 0 - 2
mcp = MCP23017(i2c, 0x20)

mcp[0].input( pull=1 )
mcp[1].input( pull=1 )
mcp[2].input( pull=1 )

# Stepper 3 und Endschalter 3
while True:
    mcp[4].output( 1 )
    mcp[5].output( 0 )
    mcp[6].output( 0 )
    mcp[7].output( 0 )
    time.sleep( 0.005 )
    if ( mcp[2].value() == 0 ):
        break

    mcp[4].output( 0 )
    mcp[5].output( 1 )
    mcp[6].output( 0 )
    mcp[7].output( 0 )
    time.sleep( 0.005 ) 
    if ( mcp[2].value() == 0 ):
        break    

    mcp[4].output( 0 )
    mcp[5].output( 0 )
    mcp[6].output( 1 )
    mcp[7].output( 0 )
    time.sleep( 0.005 ) 
    if ( mcp[2].value() == 0 ):
        break          

    mcp[4].output( 0 )
    mcp[5].output( 0 )
    mcp[6].output( 0 )
    mcp[7].output( 1 )
    time.sleep( 0.005 )
    if ( mcp[2].input() == 0 ):
       break 
