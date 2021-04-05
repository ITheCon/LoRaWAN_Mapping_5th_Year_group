#!/usr/bin/env python

import os
from time import sleep              
import RPi.GPIO as GPIO             # Allows the GPIO pins to be called
from datetime import datetime

GPIO.setmode(GPIO.BCM)              # Set's GPIO pins to BCM GPIO numbering

# Set input pins
PIN_1 = 6                       # input 1
PIN_2 = 5                       # input 2
PIN_3 = 0                       # input 3
PIN_4 = 11                      # input 4
PIN_5 = 9                       # input 5
PIN_6 = 10                      # input 6
PIN_7 = 22                      # input 7
PIN_8 = 27                      # input 8


# Set input pins to be an input
GPIO.setup(PIN_1, GPIO.IN)      
GPIO.setup(PIN_2, GPIO.IN)      
GPIO.setup(PIN_3, GPIO.IN)      
GPIO.setup(PIN_4, GPIO.IN)      
GPIO.setup(PIN_5, GPIO.IN)      
GPIO.setup(PIN_6, GPIO.IN)      
GPIO.setup(PIN_7, GPIO.IN)      
GPIO.setup(PIN_8, GPIO.IN)      


file = open("/home/pi/data_log.csv", "a")           # Create data_log csv file
i=0
if os.stat("/home/pi/data_log.csv").st_size == 0:
        file.write("Time,PIN_1,PIN_2,PIN_3,PIN_4,PIN_5,PIN_6,PIN_7,PIN_8\n")       # title columns 


# Start an endless loop
while True: 
    # print PIN values
    print(GPIO.input(PIN_1), GPIO.input(PIN_2), GPIO.input(PIN_3), GPIO.input(PIN_4), GPIO.input(PIN_5), GPIO.input(PIN_6), GPIO.input(PIN_7), GPIO.input(PIN_8))
    i=i+1
    now = datetime.now()
    # write pin values to csv file
    file.write(str(now)+","+str(GPIO.input(PIN_1))+","+str(GPIO.input(PIN_2))+","+str(GPIO.input(PIN_3))+","+str(GPIO.input(PIN_4))+","+str(GPIO.input(PIN_5))+","+str(GPIO.input(PIN_6))+","+str(GPIO.input(PIN_7))+","+str(GPIO.input(PIN_8))+"\n")
    file.flush()
    # Sleep before restarting our loop
    sleep(1);                            



