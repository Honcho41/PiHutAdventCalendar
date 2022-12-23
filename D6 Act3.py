# Imports
from machine import ADC, Pin, PWM
import time

# Set up the LED pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Define pin for our sensor
lightsensor = ADC(Pin(26))

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

while True: # Run forever
    
    # Read sensor value and store it in a variable called 'light'
    light = lightsensor.read_u16()

    # Use the round function to limit the decimal places to 1
    lightpercent = round(light/65535*100,1)

    # Print our reading percentage with % symbol
    print(str(lightpercent) +"%")
    
    # 1 second delay between readings
    time.sleep(1)

    if lightpercent <= 30: # If percentage is less than or equal to 30
        
        red.value(1) # Red LED on
        amber.value(0)
        green.value(0)
        
        # Set PWM frequency to 1000
        buzzer.freq(1000)

        # Set PWM duty
        buzzer.duty_u16(10000)

    elif 30 < lightpercent < 60: # If percentage is between 30 and 60
        
        red.value(0)
        amber.value(1) # Amber LED on
        green.value(0)
        
        # Duty to 0 to turn the buzzer off
        buzzer.duty_u16(0)

    elif lightpercent >= 60: # If percentage is greater than or equal to 60
        
        red.value(0)
        amber.value(0)
        green.value(1) # Green LED on
        
        # Duty to 0 to turn the buzzer off
        buzzer.duty_u16(0)