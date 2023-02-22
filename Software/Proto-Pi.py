#import required modules
import board
import busio
import digitalio
import time

from board import SCL, SDA

# Documentation for drivers

# https://docs.circuitpython.org/projects/mcp4728/en/latest/api.html#implementation-notes
# https://docs.circuitpython.org/projects/mcp3xxx/en/latest/
# https://docs.circuitpython.org/projects/pca9685/en/latest/

#import drivers for ICs that are on the Proto-Pi
import adafruit_mcp4728
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

## Create the SPI bus interface
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# set chip select to 
cs = digitalio.DigitalInOut(board.D5) 

## Setup and configure PWM IC (PCA9685)
pwm = PCA9685(i2c_bus)
# Set the PWM frequency to 150 Hz.
pwm.frequency = 150

## Setup and configure DAC IC (MCP4728)
dac =  adafruit_mcp4728.MCP4728(i2c_bus)

## Setup and configure the ADAC
adc = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0
adc2 = AnalogIn(adc, MCP.P2)
adc3 = AnalogIn(adc, MCP.P3)
# Add additional channels here


### Example code to test functionality

# turn on red LED 
pwm.channels[5].duty_cycle = 0xF000

# set DAC outputs and saves settings
dac.channel_a.value = 0#65535 # Voltage = VDD
dac.channel_b.value = 0#int(65535/2) # VDD/2
dac.channel_c.value = 0 # VDD/4
dac.channel_d.value = 0 # 0V

# read from ADC 

print('Raw ADC Value: ', adc2.value)
print('ADC Voltage: ' + str(adc2.voltage) + 'V')
print('Raw ADC Value: ', adc3.value)
print('ADC Voltage: ' + str(adc3.voltage) + 'V')
