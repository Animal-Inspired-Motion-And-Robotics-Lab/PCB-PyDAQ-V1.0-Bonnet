# Raspberry Pi Data Conversion Board (ADC, DAC, PWM)

<img src="Photos/Proto-Pi-Board-Top.png?raw=true" width="500px"><br/>
<img src="Photos/Proto-Pi-Board-Bottom.png?raw=true" width="500px"><br/>

## Description

This board turns your Raspberry Pi into a prototyping powerhouse!  Now your Raspberry Pi can both read and generate analog voltages, in addition to driving PWM waveforms all using existing Python libraries! This repository includes all design files needed to immediately order and assemble the board or make further modifications!

## Features

- 26 Pin IDC Connector for easy prototyping
- 2x STEMMA QT compatible connectors (I2C, +3.3V and GND)
- 4x 12 bit ADC, DAC and PWM channels
- Easy access to SPI, I2C, UART and GPIO
- 2x general purpose PWM controlled LEDs 

## Pinout

### JP1 Connector Pinout <br/> <br/>

<img src="Photos/Pin.png?raw=true" width="500px"><br/> <br/>

| Pin | Signal
| --- | --- |
|1	|GND|
|2	|RXD 
|3	|+3.3V 
|4	|TXD | 
|5	|PWM0
|6	|PWM1
|7	|PWM2
|8	|PWM3
|9	|DAC0
|10	|DAC1
|11	|DAC2
|12	|DAC3
|13	|GPIO17
|14	|GPIO18
|15	|GND
|16	|GPIO22
|17	|SDA
|18	|SCL
|19	|+3.3V
|20	|ADC2
|21	|ADC3
|22	|ADC4
|23	|SPI_MOSI
|24	|ADC5
|25	|SPI_SCLK
|26	|SPI_MISO

## Python Drivers <br/> <br/>

The Proto-Pi board uses Python based drivers to control the ADC, DAC and PWM integrated circuits.  Make sure to install the Adafruit CircuitPython, and required dependencies [(instructions)](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi) before installing the following drivers: 

- [MCP4728](https://github.com/adafruit/Adafruit_CircuitPython_MCP4728) (12-bit, Quad DAC)
- [MCP3008](https://pypi.org/project/adafruit-circuitpython-mcp3xxx/ )  (10-bit, 8-Channel ADC )
- [PCA9685](https://github.com/adafruit/Adafruit_CircuitPython_PCA9685) (12-bit, 16-Channel PWM)

## Datasheets!

- [MCP4728](http://ww1.microchip.com/downloads/en/devicedoc/22187e.pdf) (12-bit, Quad DAC)
- [MCP3008](https://ww1.microchip.com/downloads/en/DeviceDoc/21295d.pdf)  (10-bit, 8-Channel ADC )
- [PCA9685](https://www.nxp.com/docs/en/data-sheet/PCA9685.pdf) (12-bit, 16-Channel PWM)


## License

The original board shape and connector pinout was based on the amazing [Adafruit Prototype Bonnet](https://www.adafruit.com/product/3203). Thanks Adafruit!

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
