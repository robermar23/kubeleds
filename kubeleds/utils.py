"""
Utility functions for the CLI
"""
import board
import adafruit_ws2801


odata = board.D5
oclock = board.D6
numleds = 25
bright = 0.25

Leds = adafruit_ws2801.WS2801(
    oclock, odata, numleds, brightness=bright, auto_write=False
)