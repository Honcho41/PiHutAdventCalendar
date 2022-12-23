# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Fill the strip with turquoise
strip.fill((72,209,204))

# Send the data to the strip
strip.write()
