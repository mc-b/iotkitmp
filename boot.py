#####
# Boot - wird beim Start/Reboot der Device durchlaufen. 
# 
# Dient z.B. zum Verbinden des Boards mit dem WLAN.
#

import network
import esp
esp.osdebug(None)
import gc
gc.collect()

# WLAN
ssid = 'LERNKUBE'
password = 'l3rnk4b3'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

