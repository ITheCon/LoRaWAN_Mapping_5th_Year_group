#!/usr/bin/env python

from time import sleep              
import RPi.GPIO as GPIO             # Allows the GPIO pins to be called
 
GPIO.setmode(GPIO.BCM)              # Set's GPIO pins to BCM GPIO numbering

# Set input pins
PIN_1 = 6			# input 1
PIN_2 = 5			# input 2
PIN_3 = 0			# input 3
PIN_4 = 11			# input 4
PIN_5 = 9			# input 5
PIN_6 = 10			# input 6
PIN_7 = 22			# input 7
PIN_8 = 27			# input 8

# Set input pins to be an input
GPIO.setup(PIN_1, GPIO.IN)      
GPIO.setup(PIN_2, GPIO.IN)      
GPIO.setup(PIN_3, GPIO.IN)      
GPIO.setup(PIN_4, GPIO.IN)      
GPIO.setup(PIN_5, GPIO.IN)      
GPIO.setup(PIN_6, GPIO.IN)      
GPIO.setup(PIN_7, GPIO.IN)      
GPIO.setup(PIN_8, GPIO.IN)      

# Start an endless loop

while True: 
    print(GPIO.input(PIN_1), GPIO.input(PIN_2), GPIO.input(PIN_3), GPIO.input(PIN_4), GPIO.input(PIN_5), GPIO.input(PIN_6), GPIO.input(PIN_7), GPIO.input(PIN_8))
    # Sleep before restarting our loop
    sleep(1);                            
