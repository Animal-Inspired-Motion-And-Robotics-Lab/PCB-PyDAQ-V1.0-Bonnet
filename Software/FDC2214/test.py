import fdc2214,board,busio
import time

i2c = busio.I2C(board.SCL,board.SDA)
cap = fdc2214.FDC2214(i2c)


while True:
    
    print(f"{time.monotonic():.8} sec",f"{cap.read():.8} pF")
    time.sleep(.5)

