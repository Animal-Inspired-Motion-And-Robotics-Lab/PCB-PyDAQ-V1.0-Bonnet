#import required modules
import board
import busio
import digitalio

# configure GPIO17 to control CP_EN, set pin high
cp_en = digitalio.DigitalInOut(board.D17)
cp_en.direction = digitalio.Direction.OUTPUT
cp_en.value = True

# message to send to HV boost converter
msg = bytes([0x00, 0xE4]) # turn on the HV supply
#msg = bytes([0x00, 0xE0]) # turn off the HV supply

# configure pin D6 as CS
cs = digitalio.DigitalInOut(board.D6)
cs.direction = digitalio.Direction.OUTPUT
cs.value = True

## Create the SPI bus interface
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

while not spi.try_lock():
    pass

try:
    # configure the SPI bus for action
    spi.configure(baudrate=1000000, phase=0, polarity=0)
    # send CS pin low
    cs.value = False
    # buffer for storing results
    result = bytearray(2)
    # send data to the HV Boost Converter (HV56020), and read results
    spi.write_readinto(msg,result)
    # send CS high
    cs.value = True
    # print out the results
    print(result)
    
finally:
    spi.unlock()
    # disable high voltage output
    #cp_en.value = False