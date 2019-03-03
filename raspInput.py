# Script to read raspPi GPIO input. Written for reading IED detection circuitry output.
# IED Detection circuitry should output high (3.3V) when detection is made and low (0V) when no detection is made.
# Script only checks if GPIO input is high at the moment the loop is run 

import time
from time import sleep
import os
import RPi.GPIO as GPIO

seconds = 1 				   # time to sleep before reading GPIO again in while loop
GPIO.setmode(GPIO.BCM)  	   # Set's GPIO pins to BCM GPIO numbering
INPUT_PIN = 4           	   # Sets our input pin, in this example I'm connecting our button to pin 4. 
GPIO.setup(INPUT_PIN, GPIO.IN) # Set our input pin to be an input

# Start a loop that never ends to start reading in raspPi GPIO
while True: 
           if (GPIO.input(INPUT_PIN) == True): # Physically read the pin now
                    print('Detection')		   # Print Detection when High Voltage (3.3V) is detected at GPIO
           else:
                    print('0')				   # Print Detection when High Voltage (0V) is detected at GPIO
           sleep(seconds);           		   # Sleep before restarting while loop
