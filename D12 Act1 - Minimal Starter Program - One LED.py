# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)
        
# Select the first pixel (pixel 0)
# Set the RGB colour (red)
strip[7] = (24,5,24)

# Send the data to the strip
strip.write()
