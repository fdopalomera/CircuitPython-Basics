import board
import time
from analogio import AnalogOut, AnalogIn

light_sensor = AnalogIn(board.A8)
analog_out = AnalogOut(board.A0)

while True:
    # More light, dim the led
    output_value = 65535 - light_sensor.value
    analog_out.value = output_value
    print(output_value)