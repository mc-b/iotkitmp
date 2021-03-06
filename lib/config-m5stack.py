### Default Pins M5Stack bzw. Mapping auf IoTKitV3.1 small

DEFAULT_IOTKIT_LED1 = 27            # ohne Funktion - internes Neopixel verwenden
DEFAULT_IOTKIT_BUZZER = 27          # ohne Funktion - internen Vibrationsmotor verwenden
DEFAULT_IOTKIT_BUTTON1 = 39         # Pushbotton A unter Touchscreen M5Stack

# Port A
DEFAULT_IOTKIT_I2C_SDA = 32
DEFAULT_IOTKIT_I2C_SCL = 33

# Port B
DEFAULT_IOTKIT_PORT_B_DAC = 26
DEFAULT_IOTKIT_PORT_B_ADC = 27

# Port C
DEFAULT_IOTKIT_PORT_C_TX = 14
DEFAULT_IOTKIT_PORT_C_RX = 13

# Port D - kann auf dem Shield bei Grove A4/A5 abgegriffen werden
DEFAULT_IOTKIT_PORT_C_TX = 1
DEFAULT_IOTKIT_PORT_C_RX = 3

# L293D mit 1 x DC Motor (zweiter ohne Funktion)
DEFAULT_IOTKIT_MOTOR1_FWD = 2
DEFAULT_IOTKIT_MOTOR1_PWM = 19
DEFAULT_IOTKIT_MOTOR1_REV = 0
DEFAULT_IOTKIT_MOTOR2_FWD = -1
DEFAULT_IOTKIT_MOTOR2_PWM = -1
DEFAULT_IOTKIT_MOTOR2_REW = -1

# SPI Bus inkl. SS Pin fuer RFID Reader
DEFAULT_IOTKIT_SPI_SCLK = 18
DEFAULT_IOTKIT_SPI_MISO = 38
DEFAULT_IOTKIT_SPI_MOSI = 23
DEFAULT_IOTKIT_SPI_SS   = 25

# Servos gleich wie Port B
DEFAULT_IOTKIT_SERVO1 = 26
DEFAULT_IOTKIT_SERVO2 = 27

# ADC - Analog Pins
DEFAULT_IOTKIT_POTI = 35
DEFAULT_IOTKIT_HALL_SENSOR = 36
