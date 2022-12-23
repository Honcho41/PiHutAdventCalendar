import time
from machine import Pin
from neopixel import NeoPixel

#Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

#sleep variable to avoid putting it in on every line while tinkering
sleep = (0.01)

# variable to store i
i = 0

#variables to store LED intensity to save putting it in on every line.
red1 = 255
red2 = 50
red3 = 10
red4 = 5
red5 = 1

while True: # Run forever
    
    # while loop for the 0-14 phase
    while i < 14:
        # these 3 'if/elif' loops stop the trail LEDs from lighting at the opposite end of the lead LED.
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
            
        # this is the main loop to control the lead/trail LEDs across the strip
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
    
    #while loop for the 14-0 phase
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
