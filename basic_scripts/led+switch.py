import time
import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.LED)  # Alternative -> D13
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    led.value = switch.value
    time.sleep(.01) # debounce delay