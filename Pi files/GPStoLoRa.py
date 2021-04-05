#!/usr/bin/env python

import os
import serial
from time import sleep
from datetime import datetime

now = datetime.now()
filename = "/home/pi/data_log_" + str(now) + ".csv"
file = open(filename, "a")           # Create data_log csv file
i=0
if os.stat(filename).st_size == 0:
        file.write("Time,Lat,Long\n")       # title columns 


LoRa = serial.Serial("/dev/ttyS0", 9600)
while True:
	LoRa.write("Request data")
	received_data = LoRa.read()
	sleep(0.03)
	data_left = LoRa.inWaiting()
	received_data += LoRa.read(data_left)
	print (received_data)
	now = datetime.now()
	file.write(str(now)+","+received_data)
	file.flush()
	sleep(1)
