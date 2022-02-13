import machine

i2c = machine.SoftI2C(sda=machine.Pin(DEFAULT_IOTKIT_I2C_SDA), scl=machine.Pin(DEFAULT_IOTKIT_I2C_SCL))

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))