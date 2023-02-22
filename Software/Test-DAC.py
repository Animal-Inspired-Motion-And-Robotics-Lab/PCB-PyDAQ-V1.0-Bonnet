#import required modules
import board
import busio
import digitalio
import time
import numpy as np

from board import SCL, SDA


import adafruit_mcp4728

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

## Setup and configure DAC IC (MCP4728)
dac =  adafruit_mcp4728.MCP4728(i2c_bus)

x = np.linspace(0,2*np.pi,80)
vout = (65535/3)*(1 + np.sin(x) )

i = 0
j = 20


while True:
    #dac.channel_d.value = int(vout[i]) # lift
    dac.channel_c.value = int(vout[j]) # swing
    time.sleep(12.5/1000)
    i = ( i + 1 ) % ( len(vout) - 1 )
    j = ( j + 1 ) % ( len(vout) - 1 )