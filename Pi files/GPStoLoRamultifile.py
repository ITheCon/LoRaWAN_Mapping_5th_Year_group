#!/usr/bin/env python

import os
import serial
from time import sleep
from datetime import datetime

LoRa = serial.Serial("/dev/ttyS0", 9600)
while True:
	LoRa.write("Request data")
	received_data = LoRa.read()
	sleep(0.05)
	data_left = LoRa.inWaiting()
	received_data += LoRa.read(data_left)
	print (received_data)
	now = datetime.now()
	time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
	filename = "/home/pi/ftp/GPSdata/data_point_" + time + ".txt"
	file = open(filename, "a") 
	file.write(time + "," + received_data)
	file.flush()
	file.close()
	print ("Data saved to file: " + filename)
	sleep(1)
