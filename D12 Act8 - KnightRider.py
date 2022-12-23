import time
from machine import Pin
from neopixel import NeoPixel

#Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

sleep = (0.01)

i = 0
red1 = 255
red2 = 50
red3 = 10
red4 = 5
red5 = 1

while True: # Run forever
    
    while i < 14:
        if i == 0:
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            strip.write()
            i = i + 1
            strip.write()
            
        elif i == 1:
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            strip[i-1] = (red2,0,0)
            time.sleep(sleep)
            i = i + 1
            strip.write()
            
        elif i == 2:
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            strip[i-1] = (red2,0,0)
            time.sleep(sleep)
            strip[i-2] = (red3,0,0)
            time.sleep(sleep)
            i = i + 1
            strip.write()
            
        elif i == 3:
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            strip[i-1] = (red2,0,0)
            time.sleep(sleep)
            strip[i-2] = (red3,0,0)
            time.sleep(sleep)
            strip[i-3] = (red4,0,0)
            time.sleep(sleep)
            i = i + 1
            strip.write()
            
        elif i >= 4:
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            strip[i-1] = (red2,0,0)
            time.sleep(sleep)
            strip[i-2] = (red3,0,0)
            time.sleep(sleep)
            strip[i-3] = (red4,0,0)
            time.sleep(sleep)
            strip[i-4] = (red5,0,0)
            time.sleep(sleep)
            i = i + 1
            strip.write()
    
    while i > 0:
        if i == 14:
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            i = i - 1
            strip.write()
            
        elif i == 13:
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            strip[i+1] = (red2,0,0)
            time.sleep(sleep)
            i = i - 1
            strip.write()
            
        elif i == 12:
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            strip[i+1] = (red2,0,0)
            time.sleep(sleep)
            strip[i+2] = (red3,0,0)
            time.sleep(sleep)
            i = i - 1
            strip.write()
            
        elif i == 11:
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            strip[i+1] = (red2,0,0)
            time.sleep(sleep)
            strip[i+2] = (red3,0,0)
            time.sleep(sleep)
            strip[i+3] = (red4,0,0)
            time.sleep(sleep)
            i = i - 1
            strip.write()
            
        elif i <= 10:
            
            strip.fill((0,0,0))
            strip[i] = (red1,0,0)
            time.sleep(sleep)
            strip[i+1] = (red2,0,0)
            time.sleep(sleep)
            strip[i+2] = (red3,0,0)
            time.sleep(sleep)
            strip[i+3] = (red4,0,0)
            time.sleep(sleep)
            strip[i+4] = (red5,0,0)
            time.sleep(sleep)
            i = i - 1
            strip.write()
