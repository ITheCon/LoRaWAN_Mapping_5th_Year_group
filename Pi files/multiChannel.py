#!/usr/bin/env python

import os
import serial
from time import sleep
from datetime import datetime

def getCoord(channel):
        LoRa.write("RD " + str(channel))
        received_data = LoRa.read()
        sleep(0.05)
        data_left = LoRa.inWaiting()
        received_data += LoRa.read(data_left)
        return received_data

def saveData(data, channel):
        now = datetime.now()
        time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        filename = "/home/pi/ftp/GPSdata/c" + str(channel)  + "_data_point_" + time + ".txt"
        file = open(filename, "a")
        file.write("c" + str(channel) + "," + time + "," + data)
        file.flush()
        file.close()

LoRa = serial.Serial("/dev/ttyS0", 9600)
transaction = 0
channels = 2
while True:
	transaction += 1
	print ("------------ Transaction " + str(transaction) + " ------------")
	for channel in range(1, channels+1):
		data = getCoord(channel)
		print ("T" + str(transaction) + ": Channel " + str(channel) + ": " + data)
		saveData(data, channel)
	        print ("T" + str(transaction) + ": Saved")
	print ("---------------------------------------")
	sleep(1)

