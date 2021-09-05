import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A1)

def get_voltage(pin):
    # Map 12-bit data to voltage (0-3.3V)
    return (pin.value * 3.3) / 65536 

while True:
    print(get_voltage(analog_in))
    time.sleep(.1) # read 10 times per second